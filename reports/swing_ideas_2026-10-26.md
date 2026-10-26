# Swing Trading Ideas — All 11 Sectors
**Generated:** 2026-10-26 10:08 UTC (Monday, pre-market)
**Price data as-of:** Friday 2026-10-23 close (last completed session — no Monday bars exist yet)
**Method:** swing-idea-engine skill (Regime → Coil → Level → Trigger), levels from live feeds only
**Not financial advice.** Educational analysis. All levels expire at the next session's open.

---

## ⚠️ Data-source status (read first)

**The git repos contain NO market data** — `swing-idea-engine` holds only the skill
(SKILL.md + 4 scripts), and `claude-trading-skills` holds skill tooling with an empty
`state/` and no `reports/`. There is nothing stale to refresh; there was never a stored
dataset. All numbers below were retrieved live this session.

| Source | Status | Used for |
|---|---|---|
| Massive MCP (`/v2/aggs`) | ✅ Working (rate-limited ~5 calls/min) | 2y daily OHLCV, 29 names + SPY/QQQ |
| FMP MCP (chart-light, profile, sector perf) | 🟡 Free tier | Cross-feed close check, sector performance, some earnings |
| FMP screener / batch-quote | ❌ Plan-gated | *Could not* build the universe programmatically |
| Bigdata.com MCP | ❌ Credits exhausted | *Could not* run the 11-sector screener |
| Yahoo / Stooq / CNBC / Nasdaq (direct) | ❌ Blocked by network policy (403) | Skill's bundled fetchers cannot reach the internet |

**Consequence:** the skill's scripts were fed CSVs built from Massive data instead of their
own Yahoo fetch. The *candidate universe* (29 liquid US large/mid caps, 2–4 per sector) was
chosen heuristically because both sector screeners were unavailable — so this is **not an
exhaustive sector screen**. Every price level, however, is traced to live retrieved data;
none is from model memory.

**To fix:** top up Bigdata.com credits, or upgrade FMP to Starter+ for the stock screener.
Either would let the engine screen the full sector universe instead of a curated subset.

---

## STEP 0 — Market regime: SELECTIVE / CAUTION-leaning

| Index | Close | vs 50-DMA | vs 200-DMA | Position in 20-day range |
|---|---|---|---|---|
| SPY | 759.97 | −1.0% (767.81) | +4.5% (727.01) | ~6% (near the low) |
| QQQ | 704.40 | −3.0% (725.81) | +4.0% (677.30) | ~5% (near the low) |

Both indices sit **below their 50-day, above their 200-day, at the bottom of their 20-day
range** — a pullback inside an intact longer-term uptrend. Per the skill's rule this is
**SELECTIVE/MIXED**: longs are lower-odds, demand better zones and tighter risk, and
**confirmation entries are the default over limit-in entries**.

Sector performance, 2026-10-23, one day, NASDAQ-listed averages only (FMP):
Energy **+3.09%** (leader) · Financial Services +1.02% · Technology +0.76% · Real Estate
+0.46% · Industrials +0.18% · Communication Services +0.15% · Basic Materials −0.12% ·
Consumer Cyclical −0.27% · Healthcare −0.30% · Utilities −0.31% · Consumer Defensive **−1.34%**.

---

## ⚠️ The strict OTA zone gate cuts almost everything

The skill's `zone_scanner.py` was run on the five most promising names. Under the Seiden/OTA
gates (**live zone + core score ≥6/9 + R:R ≥3:1 to the actual stop + correct side of price**):

| Name | Scanner result | Verdict |
|---|---|---|
| TJX | **Live DBD supply 164.17–167.28, core 6/9, Med confidence** | Only gated zone found — but it's *supply* (above price) |
| TGT | RBR demand 150.32–155.69, core 3/9, price inside zone, tested 6× | CUT — core <6/9 |
| DE | Only an invalidated DBR @ 574.45 (closed through 2026-05-21) | CUT — no live zone |
| NVDA | Only an invalidated RBD @ 209.25 (tested 11×) | CUT — no live zone |
| SLB | All zones core 3–4/9, demand zone tested 3× and 11% below price | CUT — core <6/9 |

**So: zero long setups pass the full OTA gate.** An empty Table 1 is a valid output for this
skill, and that is the honest strict answer. The ideas below are therefore **structure-based**
(swing pivots, moving averages and ATR, all live-derived) and are explicitly labelled as
*not* OTA-gated. The one live gated zone — TJX's overhead supply at 164.17 — is used to set
TJX's target, which is the proper Seiden use of it.

---

## TIER A — ideas clearing R:R ≥ 3:1 (ranked by conviction)

Conviction = coil readiness + regime alignment + R:R + earnings clarity.
Readiness: COILED ≥70, TIGHTENING 55–69, NEUTRAL 40–54, EXPANDED <40.

| # | Ticker | Sector | Setup | Entry | Stop | T1 | R:R T1 | T2 | R:R T2 | Ready | Earnings | Why |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **TJX** | Cons. Cyclical | Breakout | 148.83 | 144.93 | 162.50 | **3.51** | 164.17 | 3.93 | 66 TIGHTENING | ~Nov 18 ⚠️unverified | ATR 1.84% (6th pctile), volume 0.78× dry-up; T1 set by the only live gated supply zone |
| 2 | **DE** | Industrials | Pullback | 620.00 | 599.00 | 692.83 | **3.47** | 721.22 | 4.82 | **72 COILED** | ~Nov 25 ⚠️unverified | Highest readiness in the screen: range compression 0.60, volume 0.80× |
| 3 | **GS** | Financial | Breakout | 934.44 | 897.79 | 1077.21 | **3.89** | 1153.99 | 7.59 | 51 NEUTRAL | Reported mid-Oct ⚠️ | Financials 2nd-best sector; 20-day-high break with open space above |
| 4 | **SCHW** | Financial | Pullback | 89.50 | 86.90 | 99.13 | **3.70** | 114.53 | 9.63⚠️far | 26 EXPANDED | Reported mid-Oct ⚠️ | Sitting at the 20-day low (13% of range) in a leading sector; entry live now |
| 5 | **PLD** | Real Estate | Bounce | 123.80 | 120.40 | 136.31 | **3.68** | 146.00 | 6.53 | 23 EXPANDED | Reported 10/15 ⚠️ | 123.43 is the 10-, 20- AND 60-day low (triple-tested). **COUNTER-REGIME** (downtrend) |
| 6 | **NFLX** | Comm. Services | Bounce | 64.30 | 61.90 | 73.07 | **3.65** | 83.60 | 8.04 | 31 EXPANDED | Reported ~10/20 ⚠️ | 64.10 = 10/20/60-day low. **SPECULATIVE**: downtrend, only 3% up its 52-wk range |
| 7 | **ISRG** | Healthcare | Breakout | 459.75 | 440.31 | 528.75 | **3.55** | 603.88 | 7.41⚠️far | 37 EXPANDED | Reported ~10/21 ⚠️ | No resistance between 458 and 604 in a year. T1 is a measured move, not a prior high |
| 8 | **AMD** | Technology | Pullback | 502.60 | 473.00 | 606.20 | **3.50** | 658.52 | 5.27 | 36 EXPANDED | **11/03** — 1 day outside buffer ⚠️ | At the 20-day low, but ATR 5.66%/day. Gap risk right after the window |
| 9 | **CEG** | Utilities | Bounce | 248.00 | 232.00 | 301.77 | **3.36** | 309.80 | 3.86 | 32 EXPANDED | ~Nov 4 ⚠️unverified | Best Utilities R:R, but **COUNTER-REGIME** (downtrend) and a 21.5% wide base |
| 10 | **FCX** | Basic Materials | Pullback | 64.50 | 61.40 | 74.45 | **3.21** | 80.24 | 5.08 | 54 NEUTRAL | Reported ~10/21 ⚠️ | At the 20-day low, holding the 200-DMA (65.02) |
| 11 | **WMT** | Cons. Defensive | Breakout | 122.66 | 118.71 | 135.16 | **3.16** | — | — | 38 EXPANDED | **11/19 ✅confirmed** | +9.6% over its 50-DMA; break of the 20/60-day high at 122.40 targets the 52-wk high |

---

## TIER B — best in sector but FAILS the 3:1 gate (watch, don't size)

These are the honest cuts. Several are the *highest-quality coils in the screen* — they
simply have no 3:1 target. A rejected name with its reason is more useful than a forced pick.

| Ticker | Sector | Close | Ready | R:R T1 | R:R T2 | Why it fails |
|---|---|---|---|---|---|---|
| **TGT** | Cons. Defensive | 152.76 | **70 COILED** | 2.37 | 4.69 | Bollinger width in the **3rd percentile** — the tightest squeeze found — but it is **releasing downward**: 158.11 → 152.76 (−3.4%) on 10/23, now testing the 150.32–155.69 demand shelf from above. Needs a reclaim >155.70 (long) or a break <150.46 (short). Earnings 11/18 ✅confirmed clear |
| **NVDA** | Technology | 210.96 | 50 NEUTRAL | 2.16 | 3.87 | Resting on the 20-day low (210.18) with the 200-DMA (203.67) just beneath — a real support confluence, and earnings 11/18 ✅confirmed clear — but T1 at the 10-day high is too near for 3:1 |
| **OXY** | Energy | 64.17 | 56 TIGHTENING | 2.21 | 3.40 | Cleanest *uptrend* in the leading sector (+7.3% / +15.5% over the 50/200-DMA, 89% up its 52-wk range), but the 52-wk high at 67.45 caps the reward |
| **JPM** | Financial | 331.58 | 61 TIGHTENING | 2.49 | 5.64 | Bollinger width in the **1st percentile** — the single most squeezed name screened — but neither the pullback nor the breakout version reaches 3:1 to T1 |
| **DIS** | Comm. Services | 112.52 | 60 TIGHTENING | 1.19 | 2.09 | ATR percentile **1** (quietest in 6 months), in a clean uptrend, coiling right under the 60-day high at 113.38, earnings 11/17 ✅confirmed clear — a textbook coil with **nowhere to go**: the 52-wk high is only 4% above |
| **NEM** | Basic Materials | 108.87 | 56 TIGHTENING | 2.94 | 6.66 | Bollinger width 2nd percentile, but T1 misses 3:1 by 0.06 **and** gold miners commonly report in late October — earnings date could not be verified and may sit inside the buffer |
| **SLB** | Energy | 53.06 | 54 NEUTRAL | ~2.0 | — | Broke out +7.1% on 10/23 on 19.1M shares (vs ~11.6M avg) — the coil has already **released**, straight into live DBD supply at 53.79–56.87. R:R to the nearest opposing zone is only ~2:1 |
| **O** | Real Estate | 56.89 | 27 EXPANDED | 2.86 | 5.05⚠️ | Breakout R:R only works against a target 14% away in a confirmed downtrend |
| **VST** | Utilities | 140.16 | 29 EXPANDED | 2.72 | 3.16 | Downtrend, 20% wide base — no coil, no edge |
| **GE** | Industrials | 285.64 | 33 EXPANDED | 4.69 | 12.2⚠️ | R:R passes on paper but −27% from the 60-day high in a sharp decline; T2 is a stale far target |

---

## Cut in validation — with reasons

| Ticker | Reason |
|---|---|
| **XOM** | Earnings **2026-10-30** (confirmed) — inside the 5-trading-day buffer. Would otherwise have ranked: 99% up its 52-wk range, +10.5%/+19.6% over the 50/200-DMA, in the leading sector |
| **GOOGL** | Earnings **2026-10-28** (confirmed) — inside the buffer. At its 20-day low (320.18), below both the 50- and 200-DMA |
| **HD** | Breakout R:R 2.60 — fails |
| **UNP** | R:R 1.70 breakout / 1.90 pullback — fails both; no coil (readiness 35) |
| **COST** | Breakout R:R 2.98 — fails by 0.02 |
| **UNH** | ATR percentile **92** — maximally *expanded*, readiness 8. No setup; a move is already underway |
| **PANW** | 22.8% wide base, mid-range (pos20 47) — no contraction, no level at hand |
| **FANG** | Breakout R:R 1.04 — fails; pullback T1 2.20 |

---

## Footer (mandatory)

- **Names cut:** 8 on gates/earnings (above) + 10 placed in Tier B for failing R:R ≥3:1.
  **Zero** names pass the full OTA zone gate (core ≥6/9 + live zone + 3:1); Tier A is
  structure-based, not zone-gated, and is labelled as such.
- **Cross-feed verification (Step 3):** SPY, TGT, NVDA and GS closes matched **exactly**
  across two independent providers (Massive and FMP) — e.g. SPY 759.97 / 33,423,223 shares on
  both. **AGREE.** DE, TJX and NEM returned plan-denials from FMP, so those are
  **ONE-SOURCE (Massive only) — verify manually before order entry.**
- **Readiness method:** DE/TGT/TJX/NVDA readiness came from the skill's own
  `squeeze_scan.py`. Other names used a SQL re-implementation of the same formula,
  cross-validated on SLB (script 51.5 vs SQL 54; BB percentile 24.6 vs 25, volume ratio
  0.91 vs 0.91, range compression 1.34 vs 1.34).
- **Earnings coverage is incomplete.** FMP's free tier returns only ~10 symbols per day
  query. Confirmed clear: NVDA 11/18, TGT 11/18, DIS 11/17, WMT 11/19, CSCO 11/11.
  Confirmed inside buffer: XOM 10/30, GOOGL 10/28. **Everything marked ⚠️unverified must
  have its earnings date checked before entry** — this is the single most likely way an
  idea here is wrong.
- **Entry triggers:** regime is SELECTIVE, so **confirmation entries are the default** —
  wait for price to tag the level and print a reclaim close on expanding volume. Limit-in
  resting orders are only sanctioned in a GREENLIGHT regime, which this is not.
- **Overall confidence: 0.45.** Live, cross-checked price data and a faithful coil
  calculation, but: no programmatic sector screen (both screeners unavailable), a
  heuristically-chosen 29-name universe, incomplete earnings verification, and no name
  clearing the full zone gate.
- All levels expire at the next session's open. Re-verify on TradingView before order entry.
  Single-feed risk on DE/TJX/NEM. **Not financial advice** — sizing and the decision are yours.

### Why each Tier A idea might be wrong (one line, no hedging)
1. **TJX** — the 200-DMA at 151.61 sits between entry and T1, and price has to clear it before the target is even reachable.
2. **DE** — entry is 4% below Friday's close, so the setup never triggers if the coil breaks upward instead.
3. **GS** — entry is 6.7% above spot; in a SELECTIVE tape the 20-day high may simply cap the move.
4. **SCHW** — readiness 26 means the move may already be over, not building.
5. **PLD** — a fourth test of 123.43 in a confirmed downtrend usually breaks rather than holds.
6. **NFLX** — 3% up its 52-week range is a falling knife, and the bounce target is 11% away.
7. **ISRG** — T1 is a measured move with no historical price memory behind it.
8. **AMD** — earnings land one day past the buffer with a 5.66% daily ATR; a gap can clear the stop outright.
9. **CEG** — the AI-power trade is unwinding, and a 21.5% base means the stop is 6% wide.
10. **FCX** — it is holding the 200-DMA by 0.2%, so the support is one bad session from gone.
11. **WMT** — the 52-week high at 135.16 is the only target, leaving no room if momentum stalls.
