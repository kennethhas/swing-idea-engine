# Swing Trading Ideas — All 11 Sectors
**Run:** Mon 2026-11-02 10:06 UTC (pre-open) · **Data as-of:** close Fri 2026-10-30
**Engine:** `swing-idea-engine` skill, Task A (anticipatory swing). Educational analysis, **not financial advice.**

> **Read this first — the repo has no market data.** `kennethhas/swing-idea-engine` @ `2dfdd9a`
> contains only the skill (1 SKILL.md, 2 references, 4 scripts, 1 test). There is no stored price
> history, no indicator cache and no sector analysis in it — so nothing in the repo is "stale," there
> is simply nothing there to read. Worse, the skill's own data path is **broken in this environment**:
> `zone_scanner.fetch_yahoo()` and `data_sources.fetch_cnbc_quote()` both get `403` on CONNECT from the
> egress proxy. See "Data provenance & what to fix" at the bottom.

---

## STEP 0 — Market regime: **SELECTIVE** (longs are lower-odds)

| Index | Close | vs 50-SMA | vs 200-SMA | Position in 20-day range | State |
|---|---|---|---|---|---|
| SPY | 755.72 | −1.5% | +3.7% | 17% | MIXED |
| QQQ | 690.49 | −4.8% | +1.6% | 9% | MIXED |
| SOXX | 471.51 | −10.9% | **−1.0%** | 8% | MIXED |

**Verdict: SELECTIVE — mixed tape; demand higher zone quality and tighter risk.**

Friday 2026-10-30 was an AI-capex repricing, not generalised risk-off. Intel −29% on weak guidance
(worst day since 1974 by one account), AMD −11%/−12%, NVDA −4.2%, Nasdaq Composite −2.86%, SOXX
−7.2% on the day and **~28% below its June high — the semi complex is in its own bear market** and is
the only one of the three indices trading *below* its 200-day. The Nasdaq-100 briefly traded in
correction. Reporting ties it to the gap between AI capital spending and the cash it generates.

Sector breadth the same session (FMP avg change, NASDAQ-listed): Consumer Cyclical **+1.74%**,
Energy **+1.35%**, Utilities +0.16%, Basic Materials −0.12%, Comm Services −0.18%, Consumer Defensive
−0.33%, Healthcare −0.33%, Financial −0.69%, **Technology −1.15%**, **Industrials −1.50%**,
**Real Estate −2.13%**.

**What this means for the ideas below:** every long is counter-trend against a wobbling index, so the
default entry mode is **confirmation** (wait for the reclaim close), not a resting limit order. Short
setups are with-regime.

---

## THE IDEAS, GROUPED BY SECTOR

Universe: 44 liquid names, 4 per sector, all price > $10 and ADV > 1M shares. Every level below came
out of `zone_scanner.py`; every readiness score out of `squeeze_scan.py`. **Nothing here is recalled
from memory.** `R:R` is always recomputed to the **actual stop**, not the distal line.

Legend — **✅ ACTIONABLE** = all gates passed and the level is within ~6% of price.
**🟡 LEVEL ONLY** = all gates passed but price is 10–31% away, so it is a resting order / alert, not a trade today.
**❌ NO SETUP** = failed a gate; reason given.

### ⚡ Energy — 🟡 level only (strongest sector, no entry)
The tape's leadership: COP, CVX and XOM all closed **within 0.7% of their 52-week highs**, +21% to
+27% above their 200-day, with ATR percentiles of 7–14 (coiling *at* highs, which is continuation
behaviour, not exhaustion). The problem is precisely that strength — there is no base near price.
- **CVX** — long demand **189.23**, stop 185.53, T1 236.48 · R:R **12.77** · 7/9 · **19.7% below spot**
- **XOM** — long demand **154.84**, stop 151.20, T1 188.50 · R:R **9.25** · 7/9 · 17.3% below spot
- **COP** — long demand **106.35**, stop 102.32, T1 154.28 · R:R **11.89** · 6/9 · 31.0% below spot
- *Honest read:* chasing +27%-extended energy without a level is how the sector gives it back. These
  are the levels to bid **if** we get a real pullback. SLB fails (4/9).

### 📡 Communication Services — ❌ no setup
**Every single zone detected on GOOGL, META, T and DIS is invalidated** — price has closed straight
through all of them. GOOGL scores **readiness 3/100**, the most expanded name in the whole universe
(−16.2% vs 20-SMA, −31.5% from its high, volume 1.5× normal, range 3.84× its prior band). DIS is
paradoxical: the single most volatility-compressed name in the universe (ATR percentile **0.8**,
readiness 75 COILED, uptrend) but with **no live level to trade it against**, plus earnings 2026-11-17.
- *Action:* DIS is a watch-for-the-break name, not a zone trade. Do not try to catch GOOGL.

### 🛍️ Consumer Cyclical — 🟡 level only
- **MCD** — short supply **299.36**, stop 306.83, T1 234.23 · R:R **8.72** · 6/9 · 16.0% above spot
- **TJX — CUT**, and this one hurts: it is the **most coiled name in the universe** (readiness 80,
  ATR percentile 14, volume dried to 0.58× normal). But price at 140.31 is sitting *inside* the
  138.39–141.63 supply zone — "reacting / under test, not a clean pending entry" — and T1 122.78 is
  12.5% away, unreachable before projected 2026-11-18 earnings. The trade window straddles the event.
- HD fails (5/9), AMZN has no live zone (readiness 23).

### 🧺 Consumer Defensive — 🟡 level only
- **KO** — long demand **68.92**, stop 67.11, T1 95.37 · R:R **14.61** · 7/9 · 26.7% below spot
- WMT (4/9), COST (4/9) and PG (no zone detected) all fail. WMT is readiness 70 TIGHTENING and 12%
  above its 50-day, but its only zones are invalidated.

### 💻 Technology — ✅ **ACTIONABLE (top-ranked idea)** + 🟡
- **MSFT — long demand 497.93**, stop 490.55, T1 551.15, T2 NA · **R:R 7.21** · **8/9** · High conf ·
  readiness **71 COILED** · **4.6% below spot** · **A-tier**
  *Why:* a fresh, untested DBR demand base (freshness 2/2 — no prior return has consumed the resting
  orders) that sits well above two live *weekly* demand zones (393.82, 373.49) with weekly posture in
  uptrend, so the daily level is aligned with the higher timeframe rather than fighting it. Bollinger
  width is in the **0.8th percentile** — maximum compression. Earnings risk is gone: reported
  2026-10-28 (EPS 4.89 vs 4.72 est., revenue $92.3B vs $90.6B est.), next 2027-01-27.
  *Trigger:* **confirmation** — let price tag 497.93 and print a candle closing back above the
  proximal on expanding volume. Do not rest a blind limit order into it in a SELECTIVE tape.
  *⚠️ COUNTER-REGIME:* this is a long in the sector that is actively being repriced. T1 551.15 is the
  10-month high, so T2 is honestly NA.
  *Why might this be wrong?* The leg-out only qualified at the loosened 1.25× ATR threshold, so the
  imbalance behind the base is weaker than an 8/9 implies — and no single-stock level holds if the
  whole AI-capex complex keeps de-rating.
- **MU** — long demand **762.10**, stop 694.52, T1 1108.72 · R:R **5.13** · 6/9 · 13.9% below spot.
  Readiness 65. But it is +200% off its 12-month low and the zone is 8% wide; semis are in a bear
  market. **Counter-regime, size accordingly.**
- AVGO fails (5/9 weekly) though price is sitting exactly on that zone. PANW: its only 6/9 zone is
  41% below spot with a 40:1 R:R — a stale far target, not an edge.

### 🏥 Healthcare — 🟡 level only
- **ABBV** — long demand **236.35**, stop 230.79, T1 298.74 · R:R **11.22** · **8/9** · 19.9% below spot.
  Highest-scoring demand zone in the sector, readiness 62 TIGHTENING, uptrend, within 1.3% of its high.
- LLY fails (5/9, readiness 23 EXPANDED), UNH has only invalidated zones, ISRG's live zones score 1–3/9.

### 🏢 Real Estate — 🟡 level only
- **AMT** — long demand **168.90** (weekly), stop 160.04, T1 202.50 · R:R **3.79** · **8/9** · High conf ·
  10.1% below spot. Worst sector on the day (−2.13%); readiness 24 EXPANDED, so this is a level, not a coil.
- PLD (readiness 68 TIGHTENING but **downtrend** posture, no live zone), O (4/9), WELL (5/9) all fail.

### ⛏️ Basic Materials — ❌ no setup
**No base+leg-out zone could be detected on LIN, NUE or FCX at either the 1.6× or the 1.25× ATR leg
threshold** — these are mid-range/equilibrium charts with nothing to anchor a stop to. NEM's only live
zone (weekly demand 99.89) scores 5/9. Gold hit a one-year low on Friday, which is consistent with
NEM sitting at the 14th percentile of its 20-day range.
- *Note:* LIN is readiness 62 TIGHTENING at the 92nd percentile of its 20-day range — a coil with no
  level. Same shape as DIS.

### 🏦 Financial — ✅ **ACTIONABLE** + 🟡
- **JPM — short supply 347.89**, stop 355.16, T1 325.07, T2 NA · **R:R 3.14** · **7/9** · High conf ·
  readiness **74 COILED** · **3.2% above spot** · **B-tier**
  *Why:* a fresh, untested DBD supply zone (freshness 2/2) left behind by the 2026-10-29/30 drop, and
  this is the one direction that is **with-regime** in a SELECTIVE tape. JPM closed −2.39% at 337.04
  having traded 345.29 intraday, so the zone is live and close. The other eight zones on the chart are
  all invalidated, several tested 7–8 times — this is the only shelf that still has orders behind it.
  Earnings clear: reported 2026-10-13, next 2027-01-14.
  *Trigger:* **confirmation** — needs a rally into 347.89 and a rejection candle closing back below it.
  *Why might this be wrong?* That supply shelf is three sessions old; if the index bounces hard off
  Friday's low a bank print at 337 can cut straight through it, and T1 325.07 is a swing estimate
  rather than an opposing zone.
- **SCHW** — short supply **104.63**, stop 107.69, T1 87.37 · R:R **5.64** · 7/9 · 18.8% above spot.
- **PGR** — long demand **204.87** (weekly), stop 198.30, T1 230.72 · R:R **3.93** · 6/9 · 11.4% below spot.
- GS fails — every zone invalidated, despite readiness 58 and downtrend posture.

### 💡 Utilities — ❌ no setup (the painful cut)
- **SO — CUT. It was the cleanest near-price setup in the entire universe**: long demand 90.77, stop
  89.59, T1 96.23, **R:R 4.63**, **7/9**, High confidence, readiness 59, and only **3.1% below spot**.
  **Cut on the earnings gate: Southern Company confirmed Q3 earnings for Thursday 2026-11-05** — three
  trading days away, squarely inside the 5-day buffer. Re-run this one on 2026-11-06.
- VST — supply 148.90 scores 6/9 but **R:R 1.43, fails the 3:1 gate** (the opposing zone is too close).
- CEG and NEE have no live zone.

### 🏗️ Industrials — ✅ **ACTIONABLE (marginal)** + 🟡
- **UNP — long demand 288.11**, stop 285.84, T1 314.15, T2 NA · R:R **11.47 — UNVERIFIED** · 6/9 ·
  readiness **36 EXPANDED** · 5.2% below spot · **C-tier, marginal**
  *Three honest caveats, all of which point the same way:* (1) the scanner itself flags the R:R as
  "implausibly high — target source 'recent-swing (estimate)' likely stale/far"; (2) **the stop is
  0.37× ATR14** — the zone is only 2.06 wide (0.7%) on a stock with a 2.0% average daily range, so
  routine noise takes it out before the thesis is tested; (3) readiness 36 means **the coil has already
  released — this is a level, not an anticipatory setup.**
  *Constructive fix:* widen the stop to 1× ATR (281.95). Risk becomes 6.16 and **R:R 4.23 — still
  clears the gate**, with a stop that can actually survive a session.
  *Data caveat:* **ONE-SOURCE** — the FMP cross-check quota was exhausted, so this level is backed by a
  single feed. Verify on TradingView before entry.
- **HON** — short supply **240.55**, stop 247.35, T1 196.98 · R:R **6.41** · 7/9 · High conf · 10.2% above spot.
- CAT is the sector's wreck and a warning against bottom-fishing: −20.5% vs 50-SMA, **−42.0% from its
  high**, readiness 20, ATR in the 94th percentile, and **no detectable zone**. GE fails (3/9).

---

## RANKED BY CONVICTION × RISK/REWARD

### Table 1 — Actionable now (gates passed, level within ~6% of price)

| # | Ticker | Sector | Side | Entry (proximal) | Stop (beyond distal) | T1 | T2 | **R:R (actual stop)** | Scanner R:R | Odds | Readiness | Tier | Trigger + regime | Feeds |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | Technology | LONG | **497.93** | 490.55 | 551.15 | NA | **7.21** | 7.93 | **8/9** | 71 COILED | **A** | Confirmation · ⚠️ COUNTER-REGIME | AGREE (2) |
| 2 | **JPM** | Financial | SHORT | **347.89** | 355.16 | 325.07 | NA | **3.14** | 3.45 | 7/9 | 74 COILED | **B** | Confirmation · with-regime | AGREE (2) |
| 3 | **UNP** | Industrials | LONG | **288.11** | 285.84 (→ 281.95) | 314.15 | NA | 11.47 **UNVERIFIED** (4.23 @1×ATR) | 12.64 | 6/9 | 36 EXPANDED | **C** | Confirmation · coil released — level only | ONE-SOURCE |

**Conviction order and why:** MSFT first because it is the only name where all four links of the chain
fire together — supportive higher timeframe, a genuine coil, a fresh gated level, and cleared earnings —
and it carries the highest odds score (8/9) in the whole run. JPM second: slightly lower R:R, but it is
the only idea pointing the *same way as the tape*, which in a SELECTIVE regime is worth more than a
point of R:R. UNP third and marginal: good on paper, fragile in practice.

**Robustness check** — all three still clear the 3:1 gate at a conservative 1× ATR14 stop:
MSFT 4.53 · JPM 3.27 · UNP 4.23. None of the three depends on an unrealistically tight stop to qualify.

### Table 2 — Gated levels, not yet in range (resting orders / alerts)

| Ticker | Sector | Side | Entry | Stop | T1 | R:R | Odds | Distance |
|---|---|---|---|---|---|---|---|---|
| CVX | Energy | LONG | 189.23 | 185.53 | 236.48 | 12.77 | 7/9 | −19.7% |
| ABBV | Healthcare | LONG | 236.35 | 230.79 | 298.74 | 11.22 | **8/9** | −19.9% |
| COP | Energy | LONG | 106.35 | 102.32 | 154.28 | 11.89 | 6/9 | −31.0% |
| XOM | Energy | LONG | 154.84 | 151.20 | 188.50 | 9.25 | 7/9 | −17.3% |
| MCD | Cons. Cyclical | SHORT | 299.36 | 306.83 | 234.23 | 8.72 | 6/9 | +16.0% |
| HON | Industrials | SHORT | 240.55 | 247.35 | 196.98 | 6.41 | 7/9 | +10.2% |
| SCHW | Financial | SHORT | 104.63 | 107.69 | 87.37 | 5.64 | 7/9 | +18.8% |
| MU | Technology | LONG | 762.10 | 694.52 | 1108.72 | 5.13 | 6/9 | −13.9% |
| PGR | Financial | LONG | 204.87 | 198.30 | 230.72 | 3.93 | 6/9 | −11.4% |
| AMT | Real Estate | LONG | 168.90 | 160.04 | 202.50 | 3.79 | **8/9** | −10.1% |
| KO | Cons. Defensive | LONG | 68.92 | 67.11 | 95.37 | 14.61 | 7/9 | −26.7% |

*Note on the double-digit R:R rows:* they are large because the target is a **recent-swing estimate
with no opposing zone behind it**, not because the trade is exceptional. Treat anything above ~10:1 here
as unverified reward, and size off the stop.

---

## FOOTER (mandatory)

**Names cut in validation — 30 of 44, each with its reason** (3 actionable + 11 gated-but-distant +
30 cut = 44). A rejected name with a reason is the output, not a failure to produce one.

| Cut | Reason |
|---|---|
| **SO** | Earnings **2026-11-05** (confirmed), inside the 5-trading-day buffer. Otherwise the cleanest setup in the run (7/9, R:R 4.63, 3.1% away). Re-run 2026-11-06. |
| **TJX** | Price *inside* the supply zone (not a clean pending entry) **and** T1 unreachable before projected 2026-11-18 earnings. Highest readiness in the universe (80) — watch it. |
| **VST** | R:R 1.43 < 3:1 gate (opposing zone too close). |
| **GOOGL, META, T, DIS** | Every detected zone invalidated — price closed through all of them. |
| **LIN, NUE, FCX** | No base+leg-out zone detectable at 1.6× or 1.25× ATR. Equilibrium charts. |
| **PANW** | Only 6/9 zone is 41% below spot, R:R 40:1 from a stale far target. |
| **HD, AVGO, LLY, NEM, WELL** | Odds score 5/9 < 6 gate. |
| **COST, WMT, O, SLB** | Odds score 4/9. |
| **GE, ISRG** | Odds score 3/9 or lower on live zones. |
| **GS, UNH** | All zones invalidated. |
| **CAT, AMZN, PG, PLD, CEG, NEE** | No live zone on the correct side of price. |

**Overall confidence: 0.62.** Raised by: two-feed agreement on both top names and on the regime
anchor; an independent news source corroborating the SOXX 471.51 close; and the SQL re-derivation of
the regime matching `regime_gate.py` to the decimal. Lowered by: most zones only surfaced at a
**loosened 1.25× ATR leg threshold** (the 1.6× default found almost nothing, which is itself a signal
that this tape has few clean bases); nearly every T1 is a swing estimate rather than an opposing zone;
and earnings dates for several Table-2 names could not be confirmed from a primary source.

**Standing reminders.** All levels **expire at the next session's open** — re-verify before order entry.
Levels came from a single primary feed (Massive) with a partial second-feed check (FMP); cross-check on
TradingView before risking capital. Big Picture / Arrival / Curve enhancers are first-pass heuristics
that need visual confirmation on a chart. **This is educational analysis, not financial advice** — the
trade decision and position sizing are yours.

**Not run:** Task B (the off-the-radar 3–5 year discovery list). This request was specifically for
sector swing setups. Say the word and I'll run it.

---

## DATA PROVENANCE & WHAT TO FIX

**What the repo actually holds.** `kennethhas/swing-idea-engine` @ `2dfdd9a` is skill-only:
`SKILL.md`, `references/{gates-and-scoring,anticipation}.md`, `scripts/{zone_scanner,squeeze_scan,regime_gate,data_sources}.py`,
`tests/test_anticipation.py`. No price data, no indicator cache, no sector analysis. So there was no
repo data to refresh — the question "is the repo data stale?" has the answer "the repo has never held any."

**The skill's live data path is blocked here.** Both feeds the scripts depend on are refused by this
environment's egress proxy with `403` on CONNECT:
- `query1/query2.finance.yahoo.com` — used by `zone_scanner.fetch_yahoo()`, i.e. *all four scripts*
- `quote.cnbc.com` — used by `data_sources.fetch_cnbc_quote()`, the Step-3 cross-feed check

Also blocked: stooq.com, financialmodelingprep.com, api.nasdaq.com, alphavantage, polygon. Direct HTTP
to any market data host fails.

**What I did instead.** Wrote a shim that patches `zone_scanner.fetch_yahoo` to read a local CSV cache,
then populated that cache (44 names + SPY/QQQ/SOXX, daily OHLCV 2026-01-02→2026-10-30) from the
**Massive** MCP server, with **FMP** MCP as the independent second feed for cross-checks. All four
skill scripts then ran **unmodified**, including weekly resampling for the multi-timeframe rule.

**Three fixes worth making, in priority order:**
1. **Allowlist the hosts** in the cloud environment's network policy: `query1.finance.yahoo.com`,
   `query2.finance.yahoo.com`, `quote.cnbc.com`. Cheapest fix — the skill then works as written.
2. **Add Massive/FMP as a first-class source** in `data_sources.py` and give `zone_scanner` a
   `--source {yahoo,massive,fmp}` flag. More robust than fix 1: it removes the single-point dependency
   on an unofficial feed, and gives a genuine two-provider cross-check that works in the cloud.
3. **Cosmetic but misleading:** the scanner hardcodes `data source: Yahoo Finance (<TICKER>)` into its
   output and into the Excel workbooks. The attached workbooks say "Yahoo Finance" but the bars came
   from Massive. Thread the real source name through `validate_bars()`.

**Also worth knowing:** FMP's plan blocks `quote`/`quote-short` entirely and rate-limits
`earnings-company` after a couple of calls; Massive allows roughly 5 requests/minute and does not
include the Benzinga earnings calendar. Earnings verification therefore fell back to web search, which
is what `references/gates-and-scoring.md` already recommends ("web-verify the count; don't trust memory").

### Sources
- Market context: [Investopedia/Yahoo — Oct 30 2026 tech sell-off](https://finance.yahoo.com/markets/stocks/articles/stock-market-today-nasdaq-p-123540419.html) · [TheStreet — Oct 30 2026](https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-oct-30-2026) · [24/7 Wall St — Nasdaq 100 correction](https://247wallst.com/investing/2026/10/31/the-nasdaq-100-briefly-fell-into-a-correction-as-the-ai-trade-cracks/) · [SOXX bear market](https://startupfortune.com/the-semiconductor-etf-soxx-just-fell-into-its-own-bear-market/)
- SO earnings date: [Southern Company press release — Q3 2026 earnings Nov 5](https://www.placera.se/pressmeddelanden/southern-company-southern-company-third-quarter-2026-earnings-to-be-released-november-5-20260925) · [Finviz](https://finviz.com/news/395620/southern-company-third-quarter-2026-earnings-to-be-released-november-5)
- TJX earnings (projected, unconfirmed): [AJ Bell key dates](https://www.ajbell.co.uk/market-research/sub/NYSE:TJX/company-info) · [TheRightTrader](https://therighttrader.com/earnings-calendar/tjx)
- UNP earnings: [MarketBeat](https://www.marketbeat.com/stocks/NYSE/UNP/earnings/) · [ChartRow](https://chartrow.com/quote/unp/earnings)
- Price/OHLCV: Massive MCP (primary), FMP MCP (cross-check). MSFT/JPM/SPY closes AGREE across both feeds.
