# Swing Idea Engine — Sector Sweep

**Run:** 2026-08-17 (pre-open) · **Data as-of:** 2026-08-14 close (last completed session)
**Universe:** 23 liquid large-caps, 2–3 per GICS sector · **Variant:** Balanced
**Engine:** `swing-idea-engine` — Step 0 regime → Step 1 retrieve + squeeze scan → Step 2 zone scan + gates → Step 3 validate

> Educational analysis, **not financial advice**. Every price level below was retrieved live this
> session; none come from model memory.

---

## Step 0 — Market regime: **GREENLIGHT**

| Index | Close | vs 50SMA | vs 200SMA | Posture |
|---|---|---|---|---|
| SPY | 776.34 | +3.7% | +10.0% | CONSTRUCTIVE (price > 50 > 200) |
| QQQ | 731.07 | +2.5% | +12.4% | CONSTRUCTIVE (price > 50 > 200) |

Demand-zone longs are **with-regime**. Short setups are tagged **COUNTER-REGIME**.
Caveat: SPY/QQQ sit at 94–95% of their 20-day range — constructive but *extended*, which is
precisely why so few demand zones remain live near price (see cuts).

### Sector relative strength (SPDR 3-month return)

| Leaders | | Middle | | Laggards | |
|---|---|---|---|---|---|
| XLV Health | +14.1% | XLK Tech | +5.9% | XLY Cons Cyc | −0.4% |
| XLF Financial | +13.4% | XLRE Real Est | +3.1% | XLU Utilities | −1.3% |
| XLI Industrials | +6.9% | XLB Materials | +1.7% | XLC Comm Svc | −3.6% |
| XLE Energy | +6.6% | XLP Cons Def | +1.3% | *(SPY +3.8%)* | |

---

## Table 1 — Swing setups that cleared every gate

Gates: R:R to actual stop ≥ 3:1 · core odds score ≥ 6/9 · zone live and correctly sided ·
no earnings inside 5 trading days. **A name failing any gate is cut, not downgraded.**

| # | Ticker | Sector | Side | Entry (proximal) | Stop | T1 | T2 | R:R | Odds | Coil | Tier | Trigger | Zone logic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ABBV** | Healthcare | Long | **236.35** | 230.79 | 267.47 | NA | **5.60** | **9/9** | 74 COILED | **A** | Limit-in OK (GREENLIGHT + fresh zone) | RBR demand formed 2026-06-24, **untested**; strongest sector (XLV +14.1%); price 5.3% above entry |
| 2 | **FANG** | Energy | Long | **189.63** | 184.31 | 211.69 | NA | **4.14** | 8/9 | 71 COILED | **A** | Limit-in OK, or wait for reclaim of 189.63 | DBR demand formed 2026-08-07, **untested, 1 week old**; XLE +6.6%; price 6.3% above entry |
| 3 | **DIS** | Comm Svcs | **Short** | **108.12** | 110.05 | 92.49 | NA | 8.12 | 6/9 | 41 expanded | **C** | **Confirmation only** — needs rejection candle at 108.12 | DBD supply from 2026-02-11, tested once; DIS at 98% of 20-day range into old supply. **COUNTER-REGIME** |
| 4 | **ISRG** | Healthcare | **Short** | **450.06** | 463.63 | 328.57 | NA | 8.95 | 6/9 | 41 expanded | **C** | **Confirmation only**; entry sits 14.1% above price — watch, don't stalk | DBD supply from 2026-05-08, untested; ISRG −17.3% vs 200SMA. **COUNTER-REGIME** |

**Sort order = anticipatory conviction.** #1 and #2 are the full signal firing in sequence —
coil ≥ 55 **and** fresh gated zone **and** with-regime. #3 and #4 are level-only: the zones gate,
but the coil has already released, so they carry a lower tier by construction.

### Position detail

| Ticker | Last close | Dist. to entry | Risk/share | Risk % | Sub-scores (Str/RR/Big/Fresh/Time) | Cross-feed |
|---|---|---|---|---|---|---|
| ABBV | 249.46 | −5.3% | $5.56 | 2.35% | 2 / 2 / 2 / 2 / 1 | **AGREE** (Massive 249.46 = FMP 249.46) |
| FANG | 202.47 | −6.3% | $5.32 | 2.81% | 1 / 2 / 2 / 2 / 1 | ONE-SOURCE — verify manually |
| DIS | 106.85 | +1.2% | $1.93 | 1.79% | 1 / 2 / 1 / 1 / 1 | **AGREE** (Massive 106.85 = FMP 106.85) |
| ISRG | 394.51 | +14.1% | $13.57 | 3.02% | 1 / 2 / 1 / 2 / 0 | ONE-SOURCE — verify manually |

### Why each might be wrong

- **ABBV** — the leg-out built over several candles rather than one violent one, so the imbalance
  is less concentrated than a 9/9 score implies; a drift back to 236 may find sellers, not the
  untouched bid the freshness score assumes.
- **FANG** — the zone was only detected once the leg-out threshold was loosened to 1.2× ATR
  (default 1.6), and strength scored 1/2: the departure from the level was ordinary, not violent.
- **DIS** — a six-month-old supply zone that has already absorbed one test, fading a name that
  just closed at the top of its 20-day range in a tape where the index is making highs.
- **ISRG** — the entry is 14% overhead, so the setup is a watch item, not a trade; by the time
  price arrives the zone may be five months stale and the downtrend thesis already resolved.

**Targets:** every T1 above is the 60-bar swing extreme, **not** an opposing supply/demand zone —
the scanner found no opposing zone, so these are estimates and must be confirmed on the chart.
T2 is `NA` for all four for the same reason.

---

## Table 2 — Off-the-radar discovery

**Not run.** This request was scoped to swing setups across the 11 sectors; the 3–5 year
discovery list is a separate job with a different horizon and evidence base. Available on request.

---

## Sector-by-sector: what happened to the other 19 names

| Sector | Best candidate | Verdict |
|---|---|---|
| Energy | FANG ✅ | **PASS.** XOM cut (R:R 2.43 < 3), SLB cut (R:R 2.38 < 3) — both coiled, neither pays enough |
| Communication Services | DIS ✅ | **PASS (short).** GOOGL cut — nearest live demand is 19.8% below price, R:R 20.5 flagged as artifact |
| Consumer Cyclical | HD ❌ | **CUT — reports Q2 earnings 2026-08-18 13:00 UTC, inside the 5-day buffer.** Zone was otherwise valid (core 7/9, R:R 5.98 @ 305.06). AMZN: no live zone near price |
| Consumer Defensive | — | **No setup.** PG is the most coiled name in the universe (readiness 72, at 20% of its 6-mo range) but presents **no live zone**; KO cut (core 5/9, R:R artifact) |
| Technology | — | **No setup.** AMD and MU have run too far — nearest live demand sits 19% below price with R:R > 10, flagged UNVERIFIED |
| Healthcare | ABBV ✅ ISRG ✅ | **2 PASS.** The RS leader also produced the only 9/9 zone in the sweep |
| Real Estate | — | **No setup.** Neither AMT nor PLD has a live, correctly-sided zone within 20% of price on any window or threshold |
| Basic Materials | — | **No setup.** FCX cut (core 4/9); NEM readiness 40 (expanded, +29.6% in a month) and its weekly zone pays only 2.86:1 |
| Financial | — | **No setup.** JPM is the most coiled name in the sweep (readiness 85) but its zone scores 4/9 with R:R 2.14; SCHW's zone is 12.7% away with an artifact R:R |
| Utilities | — | **No setup.** NEE has no live zone; VST cut (core 5/9, R:R artifact) |
| Industrials | — | **No setup.** Neither CAT nor ETN has a live, correctly-sided zone within 20% of price |

---

## Footer — validation log

**Names cut in validation: 19 of 23.**

- **1 cut on the earnings gate:** HD (reports 2026-08-18, confirmed via events calendar).
- **6 cut on R:R < 3:1 to the actual stop:** XOM (2.43), SLB (2.38), JPM (2.14), NEM (2.86),
  HD-alt zones, KO-alt zones.
- **5 cut on core score < 6/9:** JPM (4), FCX (4), VST (5), KO (5), HD's 1.3× zone (3).
- **5 cut as R:R artifacts (>10:1 from a stale/far target):** GOOGL, AMD, MU, SCHW, KO.
- **8 cut for no live, correctly-sided zone** on any window (1y / 6mo / 3mo) or leg-out
  threshold (1.6 / 1.3 / 1.2): PG, AMZN, AMT, PLD, CAT, ETN, NEE, HD-6mo.

**Overall confidence: 0.55.** Two clean anticipatory longs is a thin but honest yield, and it is
the *expected* yield in this tape: with SPY at 94% of its 20-day range, most demand zones have
already been consumed. Confidence is capped below 0.7 by three things — every T1 is a swing
estimate rather than an opposing zone; two of four survivors are single-feed; and the two best
zones required loosening the leg-out threshold below the scanner default.

**Data integrity, this run:**
- Yahoo Finance (the skill's default feed) and CNBC are **blocked by this environment's network
  policy**, so `regime_gate.py` and `data_sources.py` could not run against their normal sources.
  Bars came from the Massive market-data API instead; the regime gate's logic (price vs 50/200 SMA,
  location in 20-day range) was reproduced exactly on that feed.
- Cross-feed verification was done against FMP where the plan permitted it — **ABBV and DIS
  corroborated to the cent**; FANG, HD and ISRG were plan-denied and are tagged **ONE-SOURCE**.
- Weekly higher-timeframe context was resampled from the same daily bars (55 weekly bars), not
  fetched independently.

**Standing reminders:** all levels expire at the next session's open · re-verify every zone on
TradingView before order entry · single unofficial feed on two of four names · this is
educational analysis, **not financial advice** — sizing and the trade decision are yours.
