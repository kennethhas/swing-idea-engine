#!/usr/bin/env python3
"""
Regression tests for the continuation override (continuation_scan).
Offline-only: synthetic OHLC, no network. Run:  python tests/test_continuation.py

The invariants that matter here are the ones the override exists to enforce:
  * entry is ALWAYS above spot (never a discount limit)
  * the trigger is the NEAREST overhead level, not the highest
  * extended names are CUT, not downgraded
  * the target uses the highest CLOSE, so rejection wicks can't inflate R:R
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import continuation_scan as cs

PASS, FAIL = 0, 0
def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1; print(f"  ok   {name}")
    else:
        FAIL += 1; print(f"  FAIL {name}")

def bars_from(closes, highs=None, lows=None):
    """Build OHLC bars from a close series, with optional explicit highs/lows."""
    out = []
    for i, c in enumerate(closes):
        o = closes[i-1] if i else c
        hi = highs[i] if highs else max(o, c) * 1.006
        lo = lows[i] if lows else min(o, c) * 0.994
        out.append((f"d{i:03d}", o, hi, lo, c))
    return out

def uptrend_then_base(lo=80.0, hi=150.0, pb_to=138.0, bounce_to=143.0,
                      coil_mid=141.0, coil_amp=1.4):
    """
    The canonical continuation shape: a long uptrend to a high, a pullback, a
    bounce to a LOWER high, then a tight coil under it. The prior high stays
    overhead as the objective — which is what gives a continuation entry its R:R.
    """
    closes = [lo + (hi - lo) * i / 129 for i in range(130)]
    closes += [hi + (pb_to - hi) * (i + 1) / 12 for i in range(12)]
    closes += [pb_to + (bounce_to - pb_to) * (i + 1) / 8 for i in range(8)]
    closes += [coil_mid + coil_amp * ((i % 5) / 4.0 - 0.5) for i in range(20)]
    return bars_from(closes)

print("continuation_scan")

# --- entry side ---------------------------------------------------------
b = uptrend_then_base()
r = cs.scan(b, "TREND")
check("clean coil under a shelf produces a setup", r.get('cut') is None)
if not r.get('cut'):
    check("entry is ABOVE spot (never a discount limit)", r['trig'] > r['spot'])
    check("stop is below the trigger", r['stop'] < r['trig'])
    check("target is above the trigger", r['target'] > r['trig'])
    check("T2 is above T1", r['t2'] > r['target'])
    check("R:R recomputes from stated levels",
          abs((r['target'] - r['trig']) / r['risk'] - r['rr']) < 0.02)
    check("tier is one of A/B/C", r['tier'] in ('A', 'B', 'C'))

# --- trigger = NEAREST overhead, not the highest ------------------------
# The fixture has a 150 prior high AND a ~143 bounce high overhead. The trigger
# must be the 143 shelf (the first wall), not the 150 peak.
if not r.get('cut'):
    check("trigger picks the NEAREST wall, not the highest", r['trig'] < 145.0)
    check("the far prior high becomes the TARGET, not the entry",
          r['prior_high'] > r['trig'])

# --- no-chasing gate ----------------------------------------------------
vertical = bars_from([100 + 0.3 * i for i in range(100)] +
                     [130 + 3.5 * i for i in range(14)])
r3 = cs.scan(vertical, "VERTICAL")
check("a vertical name is CUT as extended", r3.get('cut') == 'extended — no chasing')

# --- downtrend ----------------------------------------------------------
down = bars_from([200 - 0.6 * i for i in range(130)])
r4 = cs.scan(down, "DOWN")
check("a downtrend is CUT (not a confirmed uptrend)",
      r4.get('cut') == 'not a confirmed uptrend')

# --- wick robustness ----------------------------------------------------
b5 = uptrend_then_base()
spike = list(b5)
i = 70
d, o, hi, lo, c = spike[i]
spike[i] = (d, o, hi * 1.35, lo, c)   # a single-bar rejection wick, close unchanged
r5a, r5b = cs.scan(b5, "X"), cs.scan(spike, "X")
if not r5a.get('cut') and not r5b.get('cut'):
    check("a rejection wick does NOT inflate the target",
          abs(r5a['target'] - r5b['target']) < 0.01)

# --- min-rr is honoured -------------------------------------------------
r6 = cs.scan(uptrend_then_base(), "STRICT", dict(min_rr=99.0))
check("--min-rr cuts on reward", r6.get('cut') == 'R:R too thin')

# --- short series -------------------------------------------------------
check("too little history is CUT, not crashed",
      cs.scan(bars_from([100 + i for i in range(20)]), "SHORT").get('cut')
      == 'insufficient history')

print(f"\n{PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
