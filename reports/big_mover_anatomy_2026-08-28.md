# Anatomy of the 95 → 144 movers, and a screen built from it

**Run:** 2026-08-28 · **Data:** daily bars through 2026-08-27 · **Feed:** Massive/Polygon

## Correction to what I told you last turn

I said the continuation screen "structurally cannot" find moves like this. **That is wrong for
half of them.** Here is what each looked like on 2026-03-06, the launch point:

| | close | from 125d high | vs SMA50 | vs SMA100 | position in range | volume vs 60d |
|---|---|---|---|---|---|---|
| **PTGX** | 92.09 | −4.6% | **+8.3%** | **+9.4%** | **89%** | **0.72** |
| **ARCB** | 93.28 | −17.4% | −0.6% | +13.6% | 63% | 0.82 |
| CVLT | 87.04 | **−56.1%** | −16.2% | **−27.5%** | **6%** | 0.98 |
| DUOL | 101.92 | **−71.1%** | −26.4% | **−44.4%** | **4%** | 1.46 |

**These are two opposite trades that got merged into one question.**

**Group A — momentum continuation (PTGX, ARCB).** Near highs, above a stacked SMA50/SMA100,
volume drying up. Both would have **passed** gate 1 and gate 2 of my continuation screen on
2026-03-06. PTGX in particular — +8.3% over its 50-day, 89% of its range, volume at 0.72× — is a
textbook version of exactly what that screen hunts for.

**Group B — crash and partial recovery (CVLT, DUOL).** Both were 56% and 71% below their highs,
deep under both moving averages, sitting at the very bottom of their range. **Both are still
below where they traded a year ago:** CVLT 140.36 today vs 179.06 last September; DUOL 142.86 vs
289.98. Buying those at 87 and 102 was buying a drawdown, not a trend. Gate 1 rejects them, and
I would defend that rejection — most −60% charts keep going.

**So the real limitation was never the entry. It was the exit.** My target model is
`T1 = highest close of 120 sessions + 0.5 ATR`. On PTGX in March that would have exited near 97
for roughly +6%, while the name went to 158. If the goal is to capture moves of this size, the
change needed is a **trailing exit**, not a different screener.

## The screen, built from the Group A signature

Market-wide over ~12,500 tickers, using grouped snapshots at 2026-03-06, 05-06, 06-26, 08-14 and
08-27. Criteria: 6-month gain ≥ 25%, price above a rising SMA100 proxy with SMA50 > SMA100,
0–12% over SMA50 (not extended), latest close at or above the prior two anchors, volume ratio
< 0.85 (dry-up), $25M–$900M daily dollar volume, price $10–600.

| Ticker | Px | 6-mo run | vs SMA50 | vs SMA100 | Vol dry-up |
|---|---|---|---|---|---|
| QURE | 49.56 | +247% | +2.1% | +17.6% | 0.15 |
| CORT | 116.93 | +245% | +10.1% | +26.1% | 0.56 |
| NAVN | 30.58 | +192% | +11.0% | +21.2% | 0.71 |
| FROG | 104.03 | +156% | +8.4% | +21.8% | 0.50 |
| TVTX | 67.52 | +148% | +7.5% | +15.8% | 0.42 |
| GEO | 32.60 | +127% | +3.8% | +12.0% | 0.36 |
| HUM | 392.63 | +119% | +1.1% | +11.2% | 0.74 |
| ELVN | 60.50 | +106% | +7.1% | +14.9% | 0.31 |
| HNGE | 92.85 | +101% | +7.0% | +17.8% | 0.44 |
| MRX | 71.38 | +100% | +3.6% | +11.2% | 0.29 |
| GH | 168.52 | +85% | +6.4% | +18.8% | 0.29 |
| NSIT | 156.26 | +84% | +9.0% | +25.3% | 0.35 |
| RHI | 44.97 | +82% | +11.5% | +22.3% | 0.49 |
| CHEF | 111.27 | +77% | +5.5% | +12.3% | 0.40 |
| ADPT | 26.44 | +78% | +10.0% | +22.2% | 0.57 |
| SN | 192.86 | +74% | +10.6% | +20.8% | 0.72 |

**This is a watchlist, not a trade list.** These are prescreen outputs on sampled anchor dates —
no entry, stop or target has been computed for them.

## Verified with real daily bars: three tested, three cut

**APGE — CUT, and this is the catch of the day.** It ranked near the top: +85% run, +0.7% over
SMA50, volume 0.65×. The daily bars say why that is fake. It gapped **90.38 → 132.60** on
2026-06-22 and has traded 132–135 every session since, with daily ranges around **0.2%**. That
is not a coil, that is **merger-arb pinning to a deal price**. A volatility-contraction screen
cannot tell a takeout from a base — both look like volatility going to zero. Any name on the list
above with a near-zero volume ratio and a flat tape needs this check before anything else.

**AXGN — CUT, extended.** +16.0% over its 50-day, past the 12% no-chasing ceiling.

**XMTR — CUT, stop too wide.** 3.83 ATR. It jumped +9.3% on 08-27 (high 98.71); the swing low is
now far below.

**Zero tradeable entries from the new list today.** The screen found the right *shape*; none of
the three verified names offers an entry at an acceptable risk right now.

## Two risks in this list worth stating plainly

1. **It is heavily biotech** — QURE, CORT, TVTX, ELVN, MRX, GH, ADPT, plus APGE. A +100% six-month
   run in biotech is usually a binary clinical or regulatory event. The quiet consolidation after
   it is not a coil building energy; it is the market waiting for the *next* binary. That is a
   different risk than a chart pattern, and a stop does not protect against a gap.
2. **Survivorship in the method itself.** I derived this signature from four names I selected
   *because they already won*. Four winners is not a sample. I have not tested how many names had
   the same March signature and went nowhere — and that number is what decides whether the
   signature is worth anything. Until that test is run, treat this as a hypothesis.

## The honest bottom line

A 60% move in six months is not a repeatable monthly event, and no screen makes it one. What is
repeatable is the *shape*: a name that has already run hard, is holding just under its highs, and
has gone quiet on volume. My screen already finds that shape. The change that would have let you
keep the PTGX move is a **trailing exit instead of a fixed T1** — that is a one-parameter change
to the target model, and it is the single highest-value thing to fix next.

*Educational analysis, not financial advice. Levels expire at the next open. Single feed.*
