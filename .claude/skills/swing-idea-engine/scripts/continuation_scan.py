#!/usr/bin/env python3
"""
continuation_scan.py — the CONTINUATION OVERRIDE screen.

Entry is a TRIGGER LEVEL ABOVE price: the nearest overhead resistance the name
must reclaim to continue its trend. Never a demand-zone limit below price.

This exists because zone entries sit 5-15% under spot and frequently never
fill — the trend continues without you. This scanner answers the different
question: "what alert do I set so I am IN when it goes?"

Gate order (a name failing any gate is CUT, not downgraded):
  1. confirmed uptrend      close > long MA, SMA50 >= long MA, close within 6% of SMA50
  2. not extended           close <= 2.2 ATR over SMA20 AND <= 12% over SMA50
  3. contraction present    ATR percentile <= 0.75 OR range-compression < 1.15
  4. trigger reachable      nearest overhead resistance <= 10% above spot
  5. stop sane              0.8 <= (trigger - stop) / ATR <= 3.0
  6. reward sufficient      R:R to T1 >= --min-rr (default 2.0)

Target model: T1 = highest CLOSE of the last 120 sessions + 0.5 ATR. Highest
close, not highest high — several names' highs are single-bar rejection wicks
that inflate R:R by 40%+. If the trigger is already above that prior high (name
at highs), T1 = trigger + base height instead. T2 = T1 + base height.

Input: a directory of CSVs named <SYMBOL>.csv with a header row containing
Date,Open,High,Low,Close (Volume optional, ignored). Every bar must be a
completed session pulled from a live feed — never a synthesized or estimated
bar. See references/continuation-override.md.

Usage:
    python scripts/continuation_scan.py --csv-dir work/csv
    python scripts/continuation_scan.py --csv-dir work/csv --min-rr 3.0 --json out.json
"""
import argparse
import csv
import datetime
import glob
import json
import os

DEFAULTS = dict(
    min_rr=2.0,
    max_ext_atr=2.2,      # max ATRs above SMA20 before it counts as chasing
    max_ext_50=12.0,      # max % above SMA50 before it counts as chasing
    max_trig_dist=10.0,   # max % above spot for the trigger to be a usable alert
    stop_atr_min=0.8,
    stop_atr_max=3.0,
    prior_high_lookback=120,
)


def load(path):
    """Read OHLC bars. Rows with unparseable numbers are skipped, not guessed."""
    bars = []
    with open(path) as f:
        for r in csv.DictReader(f):
            try:
                bars.append((r['Date'], float(r['Open']), float(r['High']),
                             float(r['Low']), float(r['Close'])))
            except (ValueError, KeyError, TypeError):
                continue
    return bars


def sma(v, n):
    if len(v) < n:
        return [None] * len(v)
    return [None] * (n - 1) + [sum(v[i - n + 1:i + 1]) / n for i in range(n - 1, len(v))]


def atr_series(bars, n=14):
    tr = []
    for i, b in enumerate(bars):
        if i == 0:
            tr.append(b[2] - b[3])
            continue
        pc = bars[i - 1][4]
        tr.append(max(b[2] - b[3], abs(b[2] - pc), abs(b[3] - pc)))
    if len(tr) < n:
        return [None] * len(tr)
    return [None] * (n - 1) + [sum(tr[i - n + 1:i + 1]) / n for i in range(n - 1, len(tr))]


def pivots(bars, k):
    """Swing highs/lows: the extreme of a 2k+1 bar window."""
    hi, lo = [], []
    for i in range(k, len(bars) - k):
        w = bars[i - k:i + k + 1]
        if bars[i][2] == max(x[2] for x in w):
            hi.append(i)
        if bars[i][3] == min(x[3] for x in w):
            lo.append(i)
    return hi, lo


def scan(bars, sym, cfg=None):
    """Return a setup dict, or a dict with 'cut' naming the gate that failed."""
    c = dict(DEFAULTS, **(cfg or {}))

    def cut(reason, **kw):
        return dict(sym=sym, cut=reason, **kw)

    if len(bars) < 60:
        return cut('insufficient history')

    C = [b[4] for b in bars]
    H = [b[2] for b in bars]
    L = [b[3] for b in bars]
    n = len(bars)
    s20, s50 = sma(C, 20), sma(C, 50)
    s100 = sma(C, 100) if n >= 100 else [None] * n
    A = atr_series(bars)
    spot, atr = C[-1], A[-1]
    if atr is None or s50[-1] is None or s20[-1] is None or atr <= 0:
        return cut('insufficient history')
    long_ma = s100[-1] if s100[-1] is not None else s50[-1]

    # --- 1) confirmed uptrend --------------------------------------------
    if not (spot > long_ma and s50[-1] > long_ma * 0.99 and spot > s50[-1] * 0.94):
        return cut('not a confirmed uptrend')

    # --- 2) not extended / no chasing ------------------------------------
    ext_atr = (spot - s20[-1]) / atr
    ext50 = (spot / s50[-1] - 1) * 100
    if ext_atr > c['max_ext_atr'] or ext50 > c['max_ext_50']:
        return cut('extended — no chasing',
                   ext50=round(ext50, 1), ext_atr=round(ext_atr, 2))

    # --- 3) contraction present ------------------------------------------
    look = min(126, n - 15)
    ap = [A[i] / C[i] * 100 for i in range(n - look, n) if A[i]]
    atrpct = atr / spot * 100
    atr_pctl = sum(1 for x in ap if x < atrpct) / len(ap) if ap else 1.0
    b1 = max(H[-20:]) - min(L[-20:])
    b2 = max(H[-40:-20]) - min(L[-40:-20]) if n >= 40 else 0
    rcomp = b1 / b2 if b2 else 9.9
    if atr_pctl > 0.75 and rcomp >= 1.15:
        return cut('no contraction — still expanding',
                   atr_pctl=round(atr_pctl, 2), rcomp=round(rcomp, 2))

    # --- 4) TRIGGER = nearest overhead resistance ------------------------
    ph3, _ = pivots(bars, 3)
    ph2, pl2 = pivots(bars, 2)
    levels = [H[i] for i in set(ph3 + ph2) if i >= n - 70 and H[i] > spot * 1.002]
    for w in (10, 20):
        h = max(H[-w:])
        if h > spot * 1.002:
            levels.append(h)
    if not levels:
        return cut('at highs — no overhead level to reclaim')
    trig = min(levels)                        # the FIRST wall overhead, not the highest
    if (trig / spot - 1) * 100 > c['max_trig_dist']:
        return cut('trigger too far to be an alert',
                   dist=round((trig / spot - 1) * 100, 1))

    # --- 5) stop under the most recent swing low -------------------------
    recent = [i for i in pl2 if i >= n - 25]
    hl = L[max(recent)] if recent else min(L[-10:])
    hl = min(hl, min(L[-3:]))                 # never above the last 3 bars' low
    stop = hl - 0.25 * atr
    risk = trig - stop
    if risk <= 0:
        return cut('stop above trigger')
    if not (c['stop_atr_min'] <= risk / atr <= c['stop_atr_max']):
        return cut('stop too wide' if risk / atr > c['stop_atr_max'] else 'stop too tight',
                   risk_atr=round(risk / atr, 2))

    prior = [L[i] for i in pl2 if i < n - 25]
    higher_low = (hl > min(prior[-10:])) if len(prior) >= 3 else True

    # --- 6) projected target ---------------------------------------------
    # Base height is measured from the SAME swing low the stop sits under, not
    # from a fixed 20-session window. A fixed window reaches back past the base
    # into whatever crash low happens to be in range (ANET's post-earnings
    # 156.84, XOM's 149.09), turning "base height" into a number that has
    # nothing to do with the base and inflating T2 by 30%+.
    base_h = trig - hl
    lb = c['prior_high_lookback']
    prior_high = max(C[-lb:]) if n >= lb else max(C)   # highest CLOSE, wick-robust
    if trig < prior_high * 0.998:
        t1 = prior_high + 0.5 * atr
    else:
        t1 = trig + base_h
    t2 = t1 + base_h
    rr = (t1 - trig) / risk
    rr2 = (t2 - trig) / risk
    if rr < c['min_rr']:
        return cut('R:R too thin', rr=round(rr, 2), trig=round(trig, 2),
                   target=round(t1, 2), risk=round(risk, 2))

    # --- core odds score (continuation-adapted, /9) ----------------------
    score = 0
    score += 2 if ext50 < 4 else (1 if ext50 < 7 else 0)                  # room to run
    score += 2 if rr >= 3 else 1                                          # reward
    score += 2 if (s100[-1] and spot > s100[-1] and s50[-1] > s100[-1]) else 1
    score += 2 if higher_low else 0                                       # structure
    score += 1 if (atr_pctl <= 0.35 or rcomp <= 0.85) else 0              # coil

    tier = 'A' if (score >= 8 and rr >= 3) else ('B' if score >= 6 else 'C')

    # History depth is not cosmetic: with n < 100 the trend gate falls back from
    # SMA100 to SMA50, which makes gate 1 nearly free (s50 > s50*0.99 is always
    # true), and with n < 120 the prior-high target is drawn from a shorter
    # window. Rows computed that way are NOT comparable to full-history rows, so
    # say so instead of printing them side by side unmarked.
    weak = []
    if s100[-1] is None:
        weak.append('trend gate fell back to SMA50 (<100 bars)')
    if n < c['prior_high_lookback']:
        weak.append(f'prior high from {n} bars, not {c["prior_high_lookback"]}')

    return dict(
        bars=n, weak=weak,
        sym=sym, asof=bars[-1][0], spot=round(spot, 2), trig=round(trig, 2),
        dist=round((trig / spot - 1) * 100, 1), stop=round(stop, 2),
        risk=round(risk, 2), risk_atr=round(risk / atr, 2),
        target=round(t1, 2), t2=round(t2, 2), rr=round(rr, 2), rr2=round(rr2, 2),
        score=score, tier=tier, atr_pctl=round(atr_pctl, 2), rcomp=round(rcomp, 2),
        ext50=round(ext50, 1), atrpct=round(atrpct, 2), hl=higher_low,
        base_h=round(base_h, 2), prior_high=round(prior_high, 2), cut=None)


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--csv-dir', required=True, help='directory of <SYMBOL>.csv OHLC files')
    p.add_argument('--min-rr', type=float, default=DEFAULTS['min_rr'],
                   help='minimum R:R to T1 (default 2.0; the zone model gates at 3.0)')
    p.add_argument('--max-ext-atr', type=float, default=DEFAULTS['max_ext_atr'])
    p.add_argument('--max-ext-50', type=float, default=DEFAULTS['max_ext_50'])
    p.add_argument('--max-trigger-dist', type=float, default=DEFAULTS['max_trig_dist'])
    p.add_argument('--json', help='also write full results (passes + cuts) to this path')
    p.add_argument('--show-cuts', action='store_true', help='print the cut log too')
    a = p.parse_args()

    cfg = dict(min_rr=a.min_rr, max_ext_atr=a.max_ext_atr,
               max_ext_50=a.max_ext_50, max_trig_dist=a.max_trigger_dist)

    paths = sorted(glob.glob(os.path.join(a.csv_dir, '*.csv')))
    if not paths:
        raise SystemExit(f'no CSVs found in {a.csv_dir}')

    passes, cuts = [], []
    for path in paths:
        sym = os.path.basename(path)[:-4]
        r = scan(load(path), sym, cfg)
        (cuts if r.get('cut') else passes).append(r)

    passes.sort(key=lambda r: (-r['score'], -r['rr']))
    h = (f"{'SYM':6}{'asof':11}{'spot':>9}{'TRIG':>9}{'d%':>6}{'stop':>9}{'risk':>7}"
         f"{'xATR':>6}{'T1':>10}{'R:R':>6}{'T2':>10}{'R2':>6}{'core':>5}{'tier':>5}")
    print(h)
    print('-' * len(h))
    for r in passes:
        print(f"{r['sym'] + ('*' if r['weak'] else ''):6}{r['asof']:11}{r['spot']:>9}"
              f"{r['trig']:>9}{r['dist']:>6}{r['stop']:>9}{r['risk']:>7}{r['risk_atr']:>6}"
              f"{r['target']:>10}{r['rr']:>6}{r['t2']:>10}{r['rr2']:>6}{r['score']:>5}"
              f"{r['tier']:>5}{r['bars']:>6}")
    print(f"\n{len(passes)} pass of {len(paths)} scanned (min R:R {a.min_rr})")

    # Staleness is an accuracy problem, not a cosmetic one: a trigger computed
    # off a bar from last week is not the level to set an alert on today.
    asof = sorted({r['asof'] for r in passes})
    if asof:
        today = datetime.date.today().isoformat()
        stale = [r['sym'] for r in passes if r['asof'] < asof[-1]]
        print(f"data as-of: {asof[0]}" + (f" .. {asof[-1]}" if len(asof) > 1 else ""))
        if asof[-1] < today:
            print(f"  WARNING: newest bar is {asof[-1]}, today is {today} — "
                  f"refresh before setting alerts.")
        if stale:
            print(f"  WARNING: mixed as-of dates; behind the newest bar: {', '.join(stale)}")
    for r in passes:
        if r['weak']:
            print(f"  * {r['sym']}: " + '; '.join(r['weak']) +
                  " — not directly comparable to full-history rows.")

    if a.show_cuts:
        print('\nCUT LOG')
        for r in sorted(cuts, key=lambda x: x['cut']):
            extra = {k: v for k, v in r.items() if k not in ('sym', 'cut')}
            print(f"  {r['sym']:6} {r['cut']:38} {extra if extra else ''}")

    if a.json:
        with open(a.json, 'w') as f:
            json.dump(dict(passes=passes, cuts=cuts, min_rr=a.min_rr), f, indent=2)
        print(f"\nwrote {a.json}")


if __name__ == '__main__':
    main()
