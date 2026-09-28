# Swing Idea Engine — Sector Sweep
**Run:** 2026-09-28 (Mon, pre-open) · **Data as-of:** 2026-09-25 close · **Source:** FMP EOD (single feed)

> **Read the Data Limits section first.** This run was materially degraded by data access:
> Yahoo/Stooq/CNBC are blocked by network policy, and the FMP plan gates most symbols.
> 3 of the 11 requested sectors could not be screened at all.

---

## STEP 0 — Regime

| Index | Close | vs 50SMA | vs 200SMA | Posture |
|---|---|---|---|---|
| SPY | 771.35 | +1.28% (761.57) | +7.36% (718.45) | **CONSTRUCTIVE** |
| QQQ | NA | NA | NA | symbol gated on this FMP plan |

SPY sits at **89% of its 20-day closing range** — high in range, not extended vs the 200SMA.

**Verdict: GREENLIGHT (single-index, reduced confidence).** Demand-zone longs are with-regime;
supply-zone shorts are counter-regime. Normally this gate reads SPY *and* QQQ; QQQ was unavailable,
so the tech-side read is missing.

**Sector performance, 2026-09-25 (FMP NASDAQ-listed averages):**
Consumer Defensive +3.14% · Basic Materials +0.64% · Technology +0.59% · Energy +0.53% ·
Utilities +0.49% · Healthcare +0.30% · Financial Services −0.02% · Industrials −0.12% ·
Communication Services −0.82% · Consumer Cyclical −0.87% · **Real Estate −2.59%**

---

## STEP 1 — Universe + pre-momentum (coil) screen

9 names retrieved with live OHLCV (107–128 daily bars each) and scored for contraction:

| Ticker | Sector | Close | Readiness | State |
|---|---|---|---|---|
| MSFT | Technology | 516.17 | 73.7 | **COILED** |
| AMZN | Consumer Cyclical | 249.67 | 73.5 | **COILED** |
| XOM | Energy | 160.59 | 61.9 | TIGHTENING |
| GOOGL | Communication Services | 343.92 | 57.1 | TIGHTENING |
| UNH | Healthcare | 376.59 | 54.1 | NEUTRAL |
| COST | Consumer Defensive | 922.77 | 53.9 | NEUTRAL |
| BA | Industrials | 198.07 | 38.4 | EXPANDED |
| INTC | Technology | 123.00 | 37.1 | EXPANDED |
| JPM | Financial | 343.06 | 25.5 | EXPANDED |

---

## STEP 3 — TABLE 1: Swing setups that cleared every gate

Gates applied: R:R ≥ 3:1 **to the actual stop** · core odds ≥ 6/9 · zone live · correct side of price ·
no earnings inside the window. **2 of 9 names survived.**

| # | Ticker | Sector | Dir | Entry (proximal) | Stop (beyond distal) | T1 | T2 | R:R | Odds | Coil | Tier | Trigger / regime | Zone logic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **XOM** | Energy | Long | **154.84** | **151.20** | **169.64** | NA | **4.07:1** | 8/9 | 61.9 TIGHTENING | **A**\* | Limit-in OK (GREENLIGHT + fresh zone); or wait for tag + reclaim close > 154.84 on expanding volume. **With-regime.** | Untested Drop-Base-Rally: base 2026-08-05→08-07, leg-out +3.4% on 08-10. Price never returned. Risk $3.64/sh. |
| 2 | COST | Consumer Defensive | Short | **995.20** | **1015.34** | **883.10** | NA | **5.57:1** | 6/9 | 53.9 NEUTRAL | **C** | Confirmation only — wait for tag + rejection close back below 995.20. **COUNTER-REGIME.** | Drop-Base-Drop supply in a 5-month downtrend (1074 → 923). Risk $20.14/sh. |

\* **XOM Tier A is conditional** — the rubric's "with the higher-timeframe trend" leg could not be verified
(see Limits: no weekly scan was possible). Daily posture is an uptrend and price is above its 50-day.

**Ranked by conviction:** XOM clearly first — fresh/untested zone, 8/9 odds, with-regime, coil building,
tight $3.64 risk. COST is a distant second and is listed only because it passes mechanically.

### Per-name detail

**1. XOM — Energy — LONG @ 154.84**
- Entry is **3.58% below** Friday's 160.59 close. This is a pullback setup; there is nothing to do until price comes back to the zone.
- Scanner headline R:R was 4.47 measured to the *distal* line. Measured to the actual stop it is **4.07** — that is the number gated on.
- T1 169.64 is the 2026-09-15 swing high. T2 is **NA** — no opposing supply zone above.
- Next earnings **2026-10-30** (est. EPS 3.62). Outside the 5-day buffer, but close the trade or re-assess before that date.
- *Why might this be wrong?* The entry requires a pullback that may never arrive while energy stays bid, and the only target is a swing-high estimate with no opposing zone behind it to anchor it.

**2. COST — Consumer Defensive — SHORT @ 995.20**
- Entry is **7.85% above** Friday's 922.77 close. Far away; this is a watch level, not an actionable order.
- Zone has been **tested twice** (freshness scored 0) — resting supply is partly consumed.
- **Only detected at a loosened leg-out threshold** (`--leg-mult 1.1`); it does not appear at the 1.6 default or at 1.3. The imbalance that formed it was weak.
- Reported earnings **2026-09-24** (EPS 6.75 vs 6.54 est.; revenue 93.87B vs 94.97B est. — beat on EPS, missed on revenue), which produced the +4.03% gap on 09-25. Next earnings **2026-12-10** — window is clear.
- *Why might this be wrong?* The zone only exists when you relax the leg-out filter below its default, and shorting into a constructive tape after a positive earnings reaction fights both the regime and the immediate flow.

---

## TABLE 2: Off-the-radar discovery — NOT RUN

The 3–5 year discovery list requires market-cap banding and analyst-coverage counts to enforce the
off-the-radar definition. Both FMP endpoints that supply those (`search-company-screener`, `analyst`)
are gated on this plan, and web search is unavailable. Producing this table would have meant inventing
market caps and coverage counts from memory — which is exactly what this engine exists to prevent.
**Empty by design, not by oversight.**

---

## Footer — cuts, limits, confidence

### Names cut in validation (7)

| Ticker | Sector | Reason |
|---|---|---|
| **MSFT** | Technology | **Closest miss.** Core 8/9, fresh DBR demand @ 497.93, COILED 73.7 — but R:R to the actual stop is **2.91**, under the 3:1 gate. The 519.40 target is a swing-high estimate sitting at the 516.17 close, so the reward leg is unverifiable. **Best watch-list name:** coil + level + regime all align; only the target is missing. |
| AMZN | Consumer Cyclical | COILED 73.5, but **zero live zones** at any threshold tested (leg-mult 1.6 / 1.3 / 1.1). No defensible level to trade against. |
| GOOGL | Communication Services | Only live zone scores **2/9** (gate is 6). All others invalidated — price has closed through them. |
| JPM | Financial | Live zones exist but R:R is **1.05** and **0.64** — opposing zone sits too close. EXPANDED (25.5). |
| BA | Industrials | Live DBD supply @ 204.80 but R:R **1.37**, under the gate. EXPANDED (38.4). |
| UNH | Healthcare | Sole zone **invalidated** — price closed through it on 2026-07-17. |
| INTC | Technology | Core **5/9** (gate is 6); zone sits 31% below price; R:R 10.92 auto-flagged UNVERIFIED as a stale-target artifact. EXPANDED (37.1) — the move from 82 → 123 has already happened. |

### Sectors that could not be screened (3 of 11)

**Real Estate, Basic Materials, Utilities — no coverage.** Every symbol probed returned
`ACCESS DENIED — requires a higher plan`:
- Real Estate: PLD, AMT, O, SPG
- Basic Materials: FCX, NEM, LIN
- Utilities: NEE, SO, DUK, VST, XLU

Sector ETFs (XLU) and QQQ are gated too, so there was no proxy fallback. These sectors are **unscreened,
not "no setups found."** Note that Real Estate was also the worst sector on 2026-09-25 (−2.59%), so it is
plausibly where the interesting setups are — and it is precisely the one this run is blind to.

### Data limits (all material)

1. **Single unofficial feed, no cross-verification.** The Step-3 cross-feed check (`data_sources.py`) returned
   **NO-DATA** for both survivors — Yahoo *and* CNBC are blocked by network policy. Every price level here is
   **one-source**. Verify on TradingView before any order entry.
2. **No weekly / higher-timeframe scan.** The engine's multi-timeframe rule (weekly = context, daily = trigger)
   could not run: fetching 2 years of weekly bars through the MCP transport was not feasible, and 107 daily bars
   resample to only ~21 weekly bars — below the 30-bar minimum. The "Big Picture" odds-enhancer scores are
   **daily-trend-derived, not HTF-confirmed.**
3. **Zone detection required loosening.** At the 1.6 default leg-out multiple, only 3 of 9 names produced any
   zone and none passed. XOM's setup surfaces at 1.3; COST's only at 1.1. This is a documented knob, but a zone
   that needs a looser filter is a weaker zone, and both are flagged accordingly.
4. **Narrow universe.** 9 names, hand-selected, not screened — the FMP stock screener is gated. Selection was by
   liquidity and sector representation, so this is **not** a systematic sweep of each sector.
5. **Regime read is SPY-only.** QQQ is gated.

### Overall confidence: **0.35**

Low. The two survivors are mechanically sound on the data retrieved, but three sectors are unscreened,
no level is cross-verified, no HTF confirmation exists, and the universe is 9 hand-picked names rather than
a screen. Treat this as two candidate levels to verify independently, not a sector-wide conclusion.

### Standing reminders
- All levels **expire at the next session's open** — re-verify zones before order entry.
- Single unofficial data feed; cross-check every price on a second source.
- Educational analysis. **Not financial advice.** Position sizing and the trade decision are yours.

### To restore full coverage
- **FMP plan upgrade** (Starter or above) unlocks the stock screener, batch quotes, technical indicators, and the
  gated symbols — this alone fixes the 3 missing sectors and the hand-picked universe.
- **Allow `query1/query2.finance.yahoo.com`** in the environment's network policy to restore the skill's native
  feed, the weekly HTF scan, and the Step-3 cross-feed verification.
