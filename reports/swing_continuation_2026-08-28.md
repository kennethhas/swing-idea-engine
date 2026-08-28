# Continuation-Override Swing Screen — refreshed + corrected

**Run:** 2026-08-28 · **Data:** all 43 names through the **2026-08-27** close (last completed
session) · **Feed:** Massive/Polygon grouped daily aggregates
**Supersedes** `swing_continuation_2026-08-26.md`, which had two defects — see *Corrections*.

## Table 1 — Swing setups (continuation triggers)

| # | Ticker | Spot | **ENTRY = trigger** | Δ | Stop | Risk | Stop ×ATR | **T1** | R:R | T2 | R2 | Core | Tier | Bars | Earnings in window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BAC** ⚠ | 61.17 | **62.12** | +1.6% | 60.84 | 1.28 | 1.22 | **65.33** | **2.51** | 66.35 | 3.30 | 8/9 | B | 103 | No — verified |
| 2 | **XOM** | 156.44 | **158.71** | +1.5% | 155.29 | 3.42 | 1.00 | **173.18** | **4.23** | 175.75 | 4.98 | 7/9 | B | 184 | No — verified |
| 3 | **AAPL** ⚠ | 314.58 | **316.29** | +0.5% | 305.48 | 10.81 | 1.77 | **343.13** | **2.48** | 352.41 | 3.34 | 7/9 | B | 96 | No — verified |

⚠ **Short history — not directly comparable to the other rows.** AAPL has 96 bars, so the
trend gate fell back from SMA100 to SMA50 (which makes gate 1 nearly free) and the
prior-high target is drawn from 96 sessions instead of 120. BAC's target is drawn from 103.
Treat AAPL's pass as provisional until its history is backfilled.

**Theses**
- **XOM** — the standout, and the only full-history row. Six straight down days took it from
  164.05 to 156.44, but it is still 4.1% above a rising 50-day (150.22) and now sits 1.0 ATR
  under the first shelf. The selloff *improved* the setup: risk fell from 5.11 to 3.42 while
  the objective held, taking R:R from 2.26 to 4.23.
- **BAC** — tightest structure in the screen (core 8/9), coiled under 62.12 with a 1.28 stop.
  Small risk, but also a small absolute move — position accordingly.
- **AAPL** — cleared its 50-day and is coiling 0.5% under 316.29. Flagged above; the pass
  leans on a weaker trend test than the others.

**Trigger mechanics:** the level is where the alert goes. Take it on a **close above** the
trigger, not an intraday poke, ideally on expanding volume. Stop goes under the marked
higher-low the same session.

## What happened to the 08-26 list

The three names from Monday, marked to market through 08-27:

| Ticker | Trigger | What happened | Result |
|---|---|---|---|
| **ANET** | 189.82 | **Fired.** Closed 190.94 on 08-25, then 202.25 / 201.09. High 206.13. | **+5.9% from the trigger ≈ +1.2R**, still open, now cut from the screen (stop would be 3.17 ATR — it has run) |
| **HWM** | 276.67 | Never triggered. High since = 271.50; fell to 261.09 on 08-24. | No trade, no loss. Now cut on R:R 1.03 |
| **XOM** | 161.67 | Never triggered. High since = 161.13 — missed by 0.54. | No trade, no loss. Re-qualifies today at a **better** level |

One of three alerts fired, and it worked. The other two never filled and cost nothing — which
is the entire argument for a trigger entry over a resting limit: the two that were wrong were
never entered.

## Table 2 — Cut log

| Ticker | Cut reason | The number |
|---|---|---|
| SCHW | R:R too thin | 0.40 — trigger 112.20, T1 114.75, risk 6.41 |
| EQIX | R:R too thin | 0.74 |
| LMT | R:R too thin | 0.79 |
| JPM | R:R too thin | 0.83 |
| **HWM** | R:R too thin | 1.03 — risk widened to 18.32 after the 08-24 drop to 261.09 |
| DIS | R:R too thin | 1.25 |
| EOG | R:R too thin | 1.49 |
| **ANET** | Stop too wide | 3.17 ATR — it already ran; the entry is behind us |
| FCX | **Extended — no chasing** | +19.8% over its 50-day, 2.87 ATR over its 20-day |
| 33 others | Not a confirmed uptrend | below the long MA or MAs unstacked |

Same pattern as Monday: the failures are **R:R**, not lack of a coil. Tight bases everywhere,
very little room between trigger and ceiling.

## Corrections to the 2026-08-26 report

**1. T2 was wrong for ANET and XOM (code bug).** Base height was computed as
`trigger − min(low of last 20 sessions)`. That window reached back *past* the base into
unrelated lows — ANET's post-earnings 156.84, XOM's 149.09 — so "base height" measured
something that was not the base:

| | T2 as published | T2 corrected | Error |
|---|---|---|---|
| ANET | 248.31 (R2 6.22) | 222.32 (R2 3.46) | +11.7% too high |
| XOM | 185.80 (R2 4.72) | 177.46 (R2 3.09) | above the 52-week high of 176.41 |
| HWM | 303.45 | 302.81 | −0.2% (its 20-day low *was* in the base) |

Base height is now measured from the same swing low the stop sits under. Fixed, with a
regression test.

**2. Entry / stop / risk / T1 / R:R were correct.** Re-derived from the raw bars and they
recompute exactly. T1 does not depend on base height whenever the trigger is below the prior
high, which was true for all three names — so the numbers that mattered for the trade were
sound. The bug lived in the stretch target.

**3. Staleness was not flagged.** The 08-26 table mixed as-of dates (HWM/ANET 08-21, XOM
08-25) without saying so, and the levels were 3–5 sessions old by the time they were read.
The scanner now prints a per-run as-of line and warns on both stale and mixed dates.

**4. Short-history rows were not flagged.** 12 of the 43 cached names carry <100 bars, which
silently weakens the trend gate. Rows built that way are now marked `*` with the reason.

## Footer

- **43 names scanned, 3 pass.** Universe is the cached working set — tilted toward energy,
  financials, defense and AI-infra. Not a systematic universe; widen before treating an empty
  result as a market-wide read.
- **R:R gate 2:1**, a stated deviation from the zone model's 3:1. Continuation entries carry
  tighter stops and nearer targets; 3:1 empties the table. Raw R:R shown for every name — at
  3:1 today you get **XOM only**.
- **Target model:** T1 = highest *close* of the last 120 sessions + 0.5 ATR. T2 = T1 + base
  height, where base height is measured from the stop's swing low.
- **Earnings:** none of BAC / XOM / AAPL appear on the FMP earnings calendar for
  2026-08-28 → 09-08. Verified this run.
- **Single feed** (Massive/Polygon) for all levels. Re-verify on TradingView before setting
  alerts. Levels expire at the next open.
- **Not financial advice.** Sizing and the decision are the trader's.
- **Confidence 0.72** — up from 0.65: the arithmetic is now regression-tested and the data is
  one session old rather than five. Still moderate on breadth for the universe reason above.
