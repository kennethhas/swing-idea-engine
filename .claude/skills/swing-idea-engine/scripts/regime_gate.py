#!/usr/bin/env python3
"""
regime_gate.py — Step 0 market-regime gate for the Swing Idea Engine.

Purpose
-------
A demand-zone long has far better odds when the broad tape is constructive, and far worse
when the index is breaking down. This computes the posture of SPY and QQQ (and optionally
the semis proxy SOXX) so Step 0 can GREENLIGHT longs, flag them COUNTER-REGIME, or favor
the short side — instead of screening in a vacuum.

Not a forecast. It's a context filter: it states where the index sits relative to its own
50/200 SMA and its recent range, deterministically. Educational, not financial advice.

Reuses zone_scanner's keyless fetch + validation (single unofficial feed; cross-check).
When that feed is unreachable, --csv / --csv-dir supply the bars instead (see
csv_fallback.py) so Step 0 degrades to offline rather than failing the whole chain.
"""

import argparse
import sys

try:
    from zone_scanner import validate_bars, sma
    from csv_fallback import DataUnavailable, build_csv_map, resolve_bars
except ImportError:
    sys.path.insert(0, __file__.rsplit("/", 1)[0])
    from zone_scanner import validate_bars, sma
    from csv_fallback import DataUnavailable, build_csv_map, resolve_bars


def posture(symbol, csv_map=None, allow_fetch=True):
    raw, source_note = resolve_bars(symbol, "daily",
                                    csv_map=csv_map, allow_fetch=allow_fetch)
    bars, warnings = validate_bars(raw, source_note)
    if len(bars) < 200:
        return {"symbol": symbol, "state": "NA", "source": source_note,
                "reason": f"insufficient history ({len(bars)} bars; need 200)"}
    price = bars[-1].c
    s50 = sma(bars, 50)[-1]
    s200 = sma(bars, 200)[-1]
    # recent posture vs 20-day high/low
    window = bars[-20:]
    hi20 = max(b.h for b in window)
    lo20 = min(b.l for b in window)
    loc = (price - lo20) / (hi20 - lo20) if hi20 > lo20 else 0.5

    if price > s50 > s200:
        state = "CONSTRUCTIVE"
        bias = "longs favored"
    elif price < s50 < s200:
        state = "BEARISH"
        bias = "longs counter-regime; shorts favored"
    else:
        state = "MIXED"
        bias = "selective; treat longs as lower-odds"

    return {
        "symbol": symbol,
        "close": round(price, 2),
        "as_of": bars[-1].date,
        "source": source_note,
        "state": state,
        "bias": bias,
        "vs_50sma": round(100 * (price / s50 - 1), 1),
        "vs_200sma": round(100 * (price / s200 - 1), 1),
        "loc_in_20d_range_pct": round(100 * loc, 0),
        "warnings": warnings,
    }


def verdict(postures):
    """Combine index postures into one Step-0 greenlight/caution flag."""
    states = [p["state"] for p in postures if p["state"] != "NA"]
    if not states:
        return "NA — could not read regime; proceed with caution and say so"
    if all(s == "CONSTRUCTIVE" for s in states):
        return "GREENLIGHT — broad tape constructive; demand-zone longs are with-regime"
    if any(s == "BEARISH" for s in states):
        return "CAUTION — at least one index bearish; tag long setups COUNTER-REGIME"
    return "SELECTIVE — mixed tape; longs are lower-odds, demand quality + tight risk"


def main():
    ap = argparse.ArgumentParser(description="Step-0 market regime gate (SPY/QQQ/SOXX posture).")
    ap.add_argument("--symbols", default="SPY,QQQ",
                    help="Index proxies to read (default SPY,QQQ; add SOXX for semis-heavy screens).")
    ap.add_argument("--csv",
                    help="CSV fallback when the live feed is unreachable: 'SYM=path[,SYM2=path2]', "
                         "or a bare path (symbol inferred from the filename).")
    ap.add_argument("--csv-dir",
                    help="Directory of <SYMBOL>.csv files to fall back on for any symbol.")
    ap.add_argument("--offline", action="store_true",
                    help="Never touch the network; require a CSV for every symbol.")
    args = ap.parse_args()

    try:
        csv_map = build_csv_map(args.csv, args.csv_dir)
    except DataUnavailable as e:
        sys.exit(str(e))

    postures = []
    for s in [x.strip() for x in args.symbols.split(",") if x.strip()]:
        try:
            postures.append(posture(s, csv_map=csv_map, allow_fetch=not args.offline))
        except (DataUnavailable, SystemExit) as e:
            postures.append({"symbol": s, "state": "NA", "reason": str(e)})

    print("Step 0 — Market Regime\n" + "-" * 60)
    for p in postures:
        if p["state"] == "NA":
            print(f"  {p['symbol']}: NA ({p.get('reason','')})")
            continue
        print(f"  {p['symbol']} @ {p['close']} ({p['as_of']}): {p['state']} — {p['bias']}")
        print(f"      vs50={p['vs_50sma']}%  vs200={p['vs_200sma']}%  "
              f"loc-in-20d-range={p['loc_in_20d_range_pct']:.0f}%")
        print(f"      source: {p.get('source','NA')}")
    print("\nVERDICT: " + verdict(postures))
    if any(str(p.get("source", "")).startswith("CSV") for p in postures):
        print("NOTE: at least one index read from CSV — levels are only as fresh as the file.")
    print("\nContext filter, not a forecast. Single unofficial feed — cross-check. Not financial advice.")


if __name__ == "__main__":
    main()
