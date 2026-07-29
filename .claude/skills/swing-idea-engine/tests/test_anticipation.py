#!/usr/bin/env python3
"""
Regression tests for the anticipatory layer (squeeze_scan, regime_gate).
Offline-only: synthetic OHLC, no network. Run:  python tests/test_anticipation.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from zone_scanner import Bar
import squeeze_scan as sq
import regime_gate as rg

PASS, FAIL = 0, 0
def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1; print(f"  ok   {name}")
    else:
        FAIL += 1; print(f"  FAIL {name}")

def make_bars(prices, vols=None):
    """Build bars from a close series; simple OHLC around each close."""
    bars = []
    for i, c in enumerate(prices):
        o = prices[i-1] if i else c
        hi = max(o, c) * 1.005
        lo = min(o, c) * 0.995
        v = (vols[i] if vols else 1_000_000)
        bars.append(Bar(f"2026-01-{i+1:02d}", o, hi, lo, c, v))
    return bars

print("squeeze_scan:")

# 1. Insufficient history -> NA
short = make_bars([10]*30)
s, d = sq.readiness(short)
check("short history returns NA", s is None and "error" in d)

# 2. A contracting series (shrinking swings + falling volume) should out-score an
#    expanding one.
import math
n = 160
contracting = [100 + (20 * math.sin(i/3)) * (1 - i/n) for i in range(n)]  # amplitude decays
falling_vol = [max(1, int(2_000_000 * (1 - i/(n*1.2)))) for i in range(n)]
expanding = [100 + (2 * math.sin(i/3)) * (1 + i/n) for i in range(n)]     # amplitude grows
rising_vol = [max(1, int(500_000 * (1 + i/n))) for i in range(n)]

sc_contract, _ = sq.readiness(make_bars(contracting, falling_vol))
sc_expand, _ = sq.readiness(make_bars(expanding, rising_vol))
check("contracting scores higher than expanding", sc_contract > sc_expand)

# 3. Score is bounded 0..100
check("score within 0..100", 0 <= sc_contract <= 100 and 0 <= sc_expand <= 100)

# 4. classify bands are monotonic
check("classify COILED at 75", "COILED" in sq.classify(75))
check("classify EXPANDED at 30", "EXPANDED" in sq.classify(30))
check("classify NA on None", sq.classify(None) == "NA")

# 5. percentile rank sanity
check("pct_rank low value", sq._pct_rank([1,2,3,4,5], 1) == 0.2)
check("pct_rank high value", sq._pct_rank([1,2,3,4,5], 5) == 1.0)

print("regime_gate:")

# 6. verdict logic
check("all constructive -> GREENLIGHT",
      "GREENLIGHT" in rg.verdict([{"state":"CONSTRUCTIVE"},{"state":"CONSTRUCTIVE"}]))
check("any bearish -> CAUTION",
      "CAUTION" in rg.verdict([{"state":"CONSTRUCTIVE"},{"state":"BEARISH"}]))
check("mixed -> SELECTIVE",
      "SELECTIVE" in rg.verdict([{"state":"MIXED"},{"state":"CONSTRUCTIVE"}]))
check("all NA -> NA verdict",
      "NA" in rg.verdict([{"state":"NA"},{"state":"NA"}]))

print("data_sources (cross-check verdict logic, offline):")
import data_sources as ds

# monkeypatch the two fetchers so we test verdict logic without network
class _B:
    def __init__(self, c): self.c=c; self.date="2026-01-01"
def _mk_yahoo(c):
    return lambda ticker, tf="daily": [_B(c)]

# AGREE: feeds within tolerance
ds.fetch_yahoo = _mk_yahoo(100.0)
ds.validate_bars = lambda bars, note: (bars, [])
ds.fetch_cnbc_quote = lambda t: {"last":100.4,"asof":"x"}
check("close feeds -> AGREE", ds.cross_check("TEST",1.0)["verdict"]=="AGREE")

# DIVERGE: feeds far apart (e.g. unadjusted split)
ds.fetch_cnbc_quote = lambda t: {"last":50.0,"asof":"x"}
check("far feeds -> DIVERGE", ds.cross_check("TEST",1.0)["verdict"]=="DIVERGE")

# ONE-SOURCE: CNBC missing
def _cnbc_fail(t): raise SystemExit("down")
ds.fetch_cnbc_quote = _cnbc_fail
check("cnbc down -> ONE-SOURCE", "ONE-SOURCE" in ds.cross_check("TEST",1.0)["verdict"])

# NO-DATA: both missing
def _yahoo_fail(ticker, tf="daily"): raise SystemExit("down")
ds.fetch_yahoo = _yahoo_fail
check("both down -> NO-DATA", ds.cross_check("TEST",1.0)["verdict"]=="NO-DATA")

print(f"\n{PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
# --- scanner drift guard (loud failure if the bundled copy diverges from siblings) ---
import hashlib, os
def _sha(p):
    return hashlib.sha256(open(p,"rb").read()).hexdigest() if os.path.exists(p) else None
_here = os.path.join(os.path.dirname(__file__), "..", "scripts", "zone_scanner.py")
_siblings = [
    "/mnt/skills/user/supply-demand-analyst/scripts/zone_scanner.py",
    "/mnt/skills/user/surge-deep-dive/scripts/zone_scanner.py",
]
_mine = _sha(_here)
_present = [(p, _sha(p)) for p in _siblings if _sha(p)]
if _present:
    print("scanner drift guard:")
    for p, h in _present:
        name = p.split("/")[4]
        check(f"zone_scanner matches {name}", h == _mine)
    print(f"\n{PASS} passed, {FAIL} failed")
    sys.exit(1 if FAIL else 0)
