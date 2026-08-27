# Continuation-Override Swing Screen

**Run:** 2026-08-26 · **Data:** through 2026-08-26 close (XOM 08-25, HWM/ANET 08-21) · **Regime:** SELECTIVE
**Override applied:** entry = a TRIGGER LEVEL ABOVE price (reclaim of the nearest overhead resistance).
No demand-zone limits below price. Anything whose only entry was a deep discount is CUT.

## Table 1 — Swing setups (continuation triggers)

| # | Ticker | Spot | **ENTRY = trigger** | Δ to trigger | Stop | Risk | Stop ×ATR | **T1 (projected)** | R:R | T2 | Core | Tier | Earnings in window |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HWM** | 271.68 | **276.67** | +1.8% | 268.70 | 7.97 | 0.91 | **297.03** | **2.55** | 303.45 | 7/9 | B | No — early Nov *(inferred, see footer)* |
| 2 | **ANET** ⭐NEW | 188.65 | **189.82** | +0.6% | 180.42 | 9.40 | 0.97 | **215.33** | **2.71** | 248.31 | 6/9 | B | No — early Nov *(inferred)* |
| 3 | **XOM** | 160.64 | **161.67** | +0.6% | 156.56 | 5.11 | 1.46 | **173.22** | **2.26** | 185.80 | 5/9 | C | No — **2026-10-30 verified** |
| 4 | AMZN | 258.63 | 266.40 | +3.0% | 255.44 | 10.96 | 1.72 | 287.21 | **1.90** | 330.63 | — | **marginal — below the 2.0 gate** | No — **2026-10-29 verified** |

**Theses (one line each)**
- **HWM** — tightest base in the screen (stop is 0.91 ATR); held a higher low at 270.89 while coiling under the 276.67 shelf, 11.9% above its 200-day. Reclaim that shelf and the Aug high at 292–297 is the objective.
- **ANET** — the only AI-infrastructure name still above both moving averages (+6.4% vs 50-day, +26% vs 200-day) while the rest of the theme broke; trigger sits 0.6% overhead, so the alert fires almost immediately on strength.
- **XOM** — three down days into a coil (readiness 71.6 COILED), holding well above a rising 50-day; 161.67 is the first shelf, and reclaiming it turns the pullback back into the trend.
- **AMZN** — same structure, but the arithmetic gives 1.90:1 to the prior-high objective. Listed for transparency, not as a trade.

**Trigger mechanics for all four:** the level is where you set the alert. Take it on a **close above** the trigger (not an intraday poke), ideally on expanding volume. Stop goes under the marked higher-low the same session.

## Table 2 — What got cut, and why (the useful half)

| Ticker | Cut reason | The number |
|---|---|---|
| JPM | R:R too thin | 0.84 — trigger 359.30, T1 368.05, risk 10.36 |
| RTX | R:R too thin | 0.51 |
| LMT | R:R too thin | 0.98 |
| BAC | R:R too thin | 1.37 — coiled hard (ATR pct 0.17) but only 3.8% of room to its high |
| GD | R:R too thin | 1.40 |
| UNH | R:R too thin | 1.63 |
| ICE | **Extended — no chasing** | +12.5% over its 50-day, 2.3 ATR over its 20-day |
| ABBV | **Extended** | 2.2 ATR over its 20-day |
| SCHW, EOG | **Extended** | +10.7% / +10.1% over 50-day |
| MRK | **Vertical** | +21% vs 50-day, +34.9% vs 200-day, ATR percentile 0.98 |
| PGR | Stop too wide | 4.41 ATR |
| MS, GE, AAPL, COST, EQIX | Not a confirmed uptrend | below the long MA or MAs unstacked |
| 30 others | Not a confirmed uptrend | mostly the broken data-center / AI-infra complex |

**The pattern in the cuts:** almost nothing failed for lack of a coil — the failures are R:R. Name after name
is basing *just* under its prior high with a pullback deep enough that the stop eats the move. That is what
this tape is: tight bases, but not much room between the trigger and the ceiling.

## Footer

- **43 names scanned, 3 pass, 1 marginal.** You asked for 3–5 new; the strict read gives **3 tradeable, of
  which only ANET is a new name.** HWM and XOM are the same tickers I gave you earlier this week but with a
  **materially different entry** — the discount limits (HWM 256.77, XOM 154.84) are replaced by triggers
  1.8% and 0.6% *above* spot. That is the override doing exactly what you asked: no waiting for fills.
- **Gate deviation, stated once:** the skill's zone model gates at 3:1. Continuation entries carry tighter
  stops and nearer targets, so a 3:1 gate returns an empty table. I gated at **2:1** and show the raw number
  for every name so you can apply your own bar.
- **Target model:** T1 = highest *close* of the last 120 sessions + 0.5 ATR (highest close, not highest high —
  several names' highs are single-bar rejection wicks that inflate R:R; UNH's 461.62 closed 38 points off its
  high). T2 = T1 + base height.
- **Earnings:** XOM (10-30) and AMZN (10-29) calendar-verified. HWM and ANET are **inferred** from
  earnings-shaped reversal bars on 08-06 and 08-05 — FMP's per-symbol endpoint is plan-blocked for both.
  Confirm before sizing.
- **Single feed** (Massive/Polygon) for all levels; cross-checks unavailable for most of these symbols.
  Re-verify on TradingView before setting alerts. Levels expire at the next open.
- **FTNT excluded** per instruction (it was not in the universe).
- **Not run:** the skill's Table 2 off-the-radar 3–5 year discovery list — this request was scoped to
  actionable swing triggers, and discovery needs a different universe (cap band + analyst-coverage filters).
  Say the word and I'll run it separately.
- **Confidence 0.65.** High on the mechanics (deterministic, re-runnable); moderate on breadth — the
  universe is the 43 names cached this week, weighted toward sectors I screened for other reasons.
