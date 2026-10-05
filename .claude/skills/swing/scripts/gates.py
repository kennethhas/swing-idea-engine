#!/usr/bin/env python3
"""
gates.py — apply Kenneth's hard swing gates mechanically and emit a verdict.

The gate table is inherited verbatim from deep-dive-swing / surge-deep-dive
(they are identical on R:R). Nothing here is discretionary: given the same
inputs it returns the same verdict, every time.

Verdict logic
-------------
  any hard-fail                -> INELIGIBLE
  price-inside-zone, or a zone
  found only on pass-2         -> WATCH (capped, can never be TRADE)
  otherwise                    -> TRADE

Short setups always carry the executability flag until confirmed.

Usage:
    python3 gates.py --direction long --price 234.69 \
        --proximal 209.17 --distal 198.95 --stop 197.93 \
        --target 253.62 --target-tf weekly --odds 8 --tested 1 \
        --bars-ltf 180 --earnings-days 45
    python3 gates.py ... --json
"""

import argparse
import json
import sys

RR_MIN = 3.0            # >= 3:1, both directions
RR_ARTIFACT = 15.0      # > ~15:1 is an artifact, flag it
ODDS_MIN = 6            # >= 6/9, Kenneth's standing gate
TESTED_MAX = 1          # tested > 1x disqualified
EARNINGS_BUFFER = 5     # trading days, shorts included
BARS_LTF_MIN = 60       # < 60 240min bars -> ineligible


def evaluate(d):
    """d: dict of inputs. Returns (verdict, gates, metrics)."""
    gates, flags = [], []
    direction = d["direction"]
    price, prox, distal, stop = d["price"], d["proximal"], d["distal"], d["stop"]
    target, odds, tested = d.get("target"), d["odds"], d["tested"]

    def add(name, ok, detail):
        gates.append({"gate": name, "status": "PASS" if ok else "FAIL", "detail": detail})
        return ok

    hard_fail = False

    # --- Bars (checked first: too little history means stop the scan) ---
    bars = d["bars_ltf"]
    if not add("Bars", bars >= BARS_LTF_MIN,
               f"{bars} LTF bars (need >= {BARS_LTF_MIN})"):
        hard_fail = True

    # --- Price inside zone -> WATCH cap, NOT a hard fail ---
    # Evaluated before side-of-price on purpose. "Inside the zone" and "wrong side
    # of price" are different states: inside means the zone is reacting / under
    # test (WATCH until price leaves and returns to a clean proximal touch), while
    # wrong-side means it is not a tradeable zone for this direction at all.
    lo, hi = min(prox, distal), max(prox, distal)
    inside = lo <= price <= hi
    add("Price-inside-zone", not inside,
        "price is INSIDE the zone - reacting / under test, WATCH only" if inside
        else "price is outside the zone (clean pending entry)")

    # --- Side of price (only meaningful once price is outside the zone) ---
    if inside:
        add("Side of price", True, "n/a - price is inside the zone (see above)")
    else:
        if direction == "long":
            side_ok = price > hi and distal < prox
            side_detail = (f"demand {distal}/{prox} below price {price}" if side_ok
                           else f"demand {distal}/{prox} is NOT below price {price}")
        else:
            side_ok = price < lo and distal > prox
            side_detail = (f"supply {prox}/{distal} above price {price}" if side_ok
                           else f"supply {prox}/{distal} is NOT above price {price}")
        if not add("Side of price", side_ok, side_detail):
            hard_fail = True

    # --- Target must exist ---
    if target is None:
        add("Target", False, "no live opposing zone in trade direction -> ineligible")
        hard_fail = True
    else:
        add("Target", True, f"{target} (from {d.get('target_tf', 'unstated')} TF)")

    # --- R:R to the ACTUAL stop ---
    risk = abs(prox - stop)
    rr = None
    if risk <= 0:
        add("R:R", False, "risk is zero or negative - stop is not beyond the proximal")
        hard_fail = True
    elif target is not None:
        reward = (target - prox) if direction == "long" else (prox - target)
        rr = reward / risk
        if not add("R:R", rr >= RR_MIN,
                   f"{rr:.2f}:1 to actual stop (need >= {RR_MIN:.0f}:1)"):
            hard_fail = True
        if rr > RR_ARTIFACT:
            flags.append(f"ARTIFACT R:R {rr:.1f}:1 (> {RR_ARTIFACT:.0f}:1) - treat as UNVERIFIED")

    # --- Freshness ---
    if not add("Freshness", tested <= TESTED_MAX,
               f"tested {tested}x (disqualified above {TESTED_MAX}x)"):
        hard_fail = True

    # --- Odds score ---
    if not add("Odds score", odds >= ODDS_MIN, f"{odds}/9 (need >= {ODDS_MIN}/9)"):
        hard_fail = True

    # --- Earnings buffer ---
    ed = d.get("earnings_days")
    if ed is None:
        add("Earnings", False, "earnings date NOT VERIFIED - treat as blocking until checked")
        hard_fail = True
    elif not add("Earnings", ed > EARNINGS_BUFFER,
                 f"{ed} trading days away (need > {EARNINGS_BUFFER})"):
        hard_fail = True

    # --- Pass-2 zone -> WATCH cap ---
    pass2 = d.get("pass2", False)
    add("Pass-2 zone", not pass2,
        "zone only found at loosened --leg-mult 1.3 -> LOW-CONVICTION, WATCH only" if pass2
        else "found on the default leg-mult pass")

    # --- Verdict ---
    if hard_fail:
        verdict = "INELIGIBLE"
    elif inside or pass2:
        verdict = "WATCH"
    else:
        verdict = "TRADE"

    if direction == "short":
        flags.append("SHORT EXECUTABILITY: unconfirmed - needs shorting enabled "
                     "AND ticker borrowable before this is actionable")

    crowd = d.get("crowd", 0)
    if crowd:
        flags.append(f"crowd overlay {crowd:+d} (modifier only - never admits a name)")

    return verdict, gates, {"rr": rr, "risk_per_share": risk if risk > 0 else None,
                            "flags": flags}


def main():
    p = argparse.ArgumentParser(description="Apply the hard swing gates and emit a verdict.")
    p.add_argument("--ticker", default="?")
    p.add_argument("--direction", required=True, choices=["long", "short"])
    p.add_argument("--price", type=float, required=True)
    p.add_argument("--proximal", type=float, required=True)
    p.add_argument("--distal", type=float, required=True)
    p.add_argument("--stop", type=float, required=True, help="just beyond the distal")
    p.add_argument("--target", type=float, help="nearest live opposing zone; omit if none exists")
    p.add_argument("--target-tf", default="unstated", help="which TF the target came from")
    p.add_argument("--odds", type=float, required=True, help="core odds score out of 9")
    p.add_argument("--tested", type=int, required=True, help="times the zone has been tested")
    p.add_argument("--bars-ltf", type=int, required=True, help="count of 240min bars")
    p.add_argument("--earnings-days", type=int,
                   help="trading days to next earnings; omit = NOT VERIFIED = blocking")
    p.add_argument("--pass2", action="store_true", help="zone only found at --leg-mult 1.3")
    p.add_argument("--crowd", type=int, default=0, choices=[-1, 0, 1])
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    verdict, gates, m = evaluate(vars(a))

    if a.json:
        print(json.dumps({"ticker": a.ticker, "direction": a.direction,
                          "verdict": verdict, "rr": m["rr"], "gates": gates,
                          "flags": m["flags"]}, indent=2))
        return 0

    print(f"\n{a.ticker}  {a.direction.upper()}  @ {a.price}")
    print("-" * 72)
    for g in gates:
        mark = "ok " if g["status"] == "PASS" else "XX "
        print(f"  {mark} {g['gate']:<20} {g['detail']}")
    if m["rr"]:
        print(f"\n  R:R to actual stop : {m['rr']:.2f}:1   "
              f"risk/share {m['risk_per_share']:.2f}")
    print(f"\n  VERDICT: {verdict}")
    for f in m["flags"]:
        print(f"  ! {f}")
    print("\nLevels expire at next session's open. Not financial advice.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
