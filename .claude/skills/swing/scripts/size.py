#!/usr/bin/env python3
"""
size.py — risk-normalized position sizing.

Neither deep-dive-swing nor surge-deep-dive defines account size or risk %, so
this never assumes one. Default output is per-$10k of equity, so the table is
valid at any account size: multiply by (your equity / 10000).

Quarter-Kelly and risk-of-ruin need a measured win rate and avg win/loss, which
only exist once trader-memory-core holds closed trades. Until then this is
fixed-fractional, and --win-rate unlocks the Kelly read.

    shares = (equity * risk_pct/100) / |entry - stop|

Usage:
    python3 size.py --entry 209.17 --stop 197.93
    python3 size.py --entry 209.17 --stop 197.93 --equity 50000 --risk-pct 1
    python3 size.py --entry 209.17 --stop 197.93 --target 253.62 \
        --win-rate 0.35 --trades 30
"""

import argparse
import sys

RISK_LADDER = [0.5, 1.0, 2.0]
KELLY_FRACTION = 0.25          # quarter Kelly
MIN_TRADES_FOR_KELLY = 20


def main():
    p = argparse.ArgumentParser(description="Risk-normalized swing position sizing.")
    p.add_argument("--entry", type=float, required=True)
    p.add_argument("--stop", type=float, required=True)
    p.add_argument("--target", type=float, help="enables payoff / breakeven math")
    p.add_argument("--equity", type=float, help="omit for the per-$10k table")
    p.add_argument("--risk-pct", type=float, help="omit to show the whole ladder")
    p.add_argument("--win-rate", type=float, help="measured win rate 0-1, from closed trades")
    p.add_argument("--trades", type=int, default=0, help="number of closed trades behind it")
    a = p.parse_args()

    risk_ps = abs(a.entry - a.stop)
    if risk_ps <= 0:
        sys.exit("entry and stop are equal - no definable risk")

    print(f"\nEntry {a.entry}   Stop {a.stop}   Risk/share {risk_ps:.2f} "
          f"({100*risk_ps/a.entry:.2f}% of entry)")

    rr = None
    if a.target:
        reward_ps = abs(a.target - a.entry)
        rr = reward_ps / risk_ps
        be = 1.0 / (1.0 + rr)
        print(f"Target {a.target}   R:R {rr:.2f}:1   "
              f"breakeven win rate {100*be:.1f}%")

    base = a.equity if a.equity else 10000.0
    label = f"${base:,.0f} equity" if a.equity else "per $10,000 of equity"
    ladder = [a.risk_pct] if a.risk_pct else RISK_LADDER

    print(f"\n  risk %   risk $    shares   position $   ({label})")
    print("  " + "-" * 52)
    for pct in ladder:
        risk_dollars = base * pct / 100.0
        shares = risk_dollars / risk_ps
        print(f"  {pct:>5.1f}%  {risk_dollars:>8.2f}  {shares:>8.2f}   "
              f"{shares * a.entry:>10.2f}")
    if not a.equity:
        print("\n  Multiply shares by (your equity / 10,000).")

    print()
    if a.win_rate is None:
        print("  Kelly: DORMANT - needs a measured win rate from closed trades.")
        print("  Log every idea via trader-memory-core; this unlocks at "
              f"~{MIN_TRADES_FOR_KELLY}+ closed trades.")
    elif a.trades < MIN_TRADES_FOR_KELLY:
        print(f"  Kelly: WITHHELD - only {a.trades} closed trades, need "
              f"{MIN_TRADES_FOR_KELLY}+. A win rate off a small sample is noise.")
    elif rr is None:
        print("  Kelly: needs --target to compute the payoff ratio.")
    else:
        w, b = a.win_rate, rr
        edge = w - (1 - w) / b
        if edge <= 0:
            print(f"  Kelly: NEGATIVE edge at {100*w:.0f}% win / {b:.2f}:1 "
                  f"- the system says do not size this at all.")
        else:
            full = edge
            quarter = full * KELLY_FRACTION
            print(f"  Kelly (full) {100*full:.2f}%   quarter Kelly "
                  f"{100*quarter:.2f}%  of equity at risk")
            print(f"  -> {(base * quarter / risk_ps):.2f} shares per "
                  f"${base:,.0f}  (n={a.trades})")
    print("\nSizing is yours to approve. Not financial advice.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
