#!/usr/bin/env python3
"""
Regression tests for target selection, R:R-to-stop, and the proximity filter.
Offline-only: synthetic OHLC, no network. Run:  python tests/test_targets.py

Covers the rule: a zone's target MUST be a real opposing live zone. When none
exists the scanner reports NO-TARGET instead of substituting a swing extreme --
the old fallback manufactured absurd R:R (e.g. 116:1) that a separate sanity
check then flagged, destroying ~46% of otherwise-live zones.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import zone_scanner as zs
from zone_scanner import Bar

PASS, FAIL = 0, 0
def check(name, cond):
    global PASS, FAIL
    if cond: PASS += 1; print(f"  ok   {name}")
    else:    FAIL += 1; print(f"  FAIL {name}")

def mk(o, h, l, c, i, vol=1_000_000):
    return Bar(f"2026-{1+i//28:02d}-{1+i%28:02d}", o, h, l, c, vol)

def flat(n, px, start=0):
    """Quiet bars: range 0.4 so ATR settles low enough for a tight base to register."""
    return [mk(px, px+0.2, px-0.2, px, start+i) for i in range(n)]

def rally_no_supply():
    """Flat -> tight 3-candle base -> violent rally -> drift to highs.

    Only upward explosive candles, so NO supply zone can form: the demand zone
    legitimately has nothing to target. This is the 'what if there is no SZ' case.
    """
    b = flat(60, 100.0)
    for i in range(3):                                   # tight base, range 0.2 < ATR
        b.append(mk(100.5, 100.6, 100.4, 100.5, 60+i))
    up = [108.0, 116.0, 124.0, 132.0, 140.0]             # leg-out
    prev = 100.5
    for i, c in enumerate(up):
        b.append(mk(prev, c+0.3, prev-0.3, c, 63+i)); prev = c
    for i, c in enumerate([141.0, 142.0, 143.0, 144.0, 145.0]):
        b.append(mk(prev, c+0.2, prev-0.2, c, 68+i)); prev = c
    return b

def scan(bars, **kw):
    a = zs.atr(bars)
    z = zs.detect_zones(bars, a, leg_mult=kw.pop("leg_mult", 1.6))
    return (zs.score_zones(bars, a, zs.sma(bars, 50), zs.sma(bars, 200), z, **kw) if z else [])

print("target selection:")

# Rally -> tight base -> hard rally. Demand zone with NOTHING above it (price ends
# at the highs), so there is no opposing supply: must be NO-TARGET, never a guess.
b = rally_no_supply()
zones = scan(b)
dem = [z for z in zones if z.zone_type == "demand"]
check("demand zone detected in rally", len(dem) >= 1)
if dem:
    z = dem[0]
    check("no opposing supply -> target is None", z.target is None)
    check("no opposing supply -> target_source 'none'", z.target_source == "none")
    check("no opposing supply -> rr_ratio None (not fabricated)", z.rr_ratio is None)
    check("no opposing supply -> rr_score 0", z.rr_score == 0)
    check("NO-TARGET flag raised", any("NO-TARGET" in f for f in z.flags))
    check("no legacy 'recent-swing' flag", not any("recent-swing" in f for f in z.flags))
    check("rr_to_stop is None when no target", z.rr_to_stop is None)

# An explicit higher-timeframe opposing level is accepted and labelled.
zones2 = scan(rally_no_supply(), opposing_levels=[("weekly", 200.0)])
dem2 = [z for z in zones2 if z.zone_type == "demand"]
if dem2:
    z2 = dem2[0]
    check("supplied HTF level becomes the target", z2.target == 200.0)
    check("target_source names the timeframe", z2.target_source == "opposing-zone (weekly)")
    check("rr_to_stop computed from the real stop",
          z2.rr_to_stop is not None and z2.rr_to_stop > 0)
    # rr_to_stop must use |entry-stop|, which is wider than |proximal-distal|
    risk_stop = abs(z2.proximal - z2.stop); risk_dist = abs(z2.proximal - z2.distal)
    check("stop sits beyond distal (risk_stop >= zone height)", risk_stop >= risk_dist)
    check("rr_to_stop <= headline rr_ratio (honest, not inflated)",
          z2.rr_to_stop <= z2.rr_ratio + 1e-9)

print("\nproximity:")
if dem:
    far = zs.distance_pct(dem[0], b[-1].c)
    check("distance_pct returns a signed % from price", isinstance(far, float))
    check("demand below price -> negative distance", far < 0)

print(f"\n{PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
