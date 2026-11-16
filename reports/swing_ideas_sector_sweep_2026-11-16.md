# Swing Idea Engine — 11-Sector Sweep

**Data as-of:** 2026-11-13 close (last completed session) · **Generated:** 2026-11-16 10:30 UTC (Mon pre-market)
**Method:** swing-idea-engine skill — Step 0 regime → Step 1 retrieve + pre-momentum coil scan → Step 2 zone scan + Seiden/OTA odds-enhancer gates → Step 3 validate
**Educational analysis, not financial advice.** All levels expire at the next session's open.

---

## ⚠️ Read this before the tables

Three things materially limit this run. They are in the footer in full; the headlines:

1. **Single data feed.** Yahoo, Stooq and CNBC are all blocked by this environment's egress policy, so the skill's own fetchers and its Step-3 cross-feed check (`data_sources.py`) could not run. Every price here comes from **one source (FMP)** and is tagged `ONE-SOURCE`. Cross-check on TradingView before any order.
2. **Three sectors could not be screened at all.** The FMP plan attached to this session only serves price history for a short allowlist of mega-caps. **Real Estate, Utilities and Basic Materials have no accessible ticker** — not one of PLD, AMT, SPG, EQIX, O / NEE, DUK, SO, CEG, VST / LIN, FCX, NEM, NUE, SHW returned data. Those three sectors are `NA`, not "no setup".
3. **Zone detection was loosened.** At the skill's default leg-multiple (1.6) over 1 year, nine of eleven names produced *no live zone at all*. The tables below use `--leg-mult 1.0 --max-base 8` over a 90-bar window. That surfaces levels, but they are **weaker imbalances than the default standard implies** — treat the core scores as generous.

---

## Step 0 — Market regime: **SELECTIVE / MIXED**

| Index | Close | vs 50-DMA | vs 200-DMA | 20-day range position |
|---|---|---|---|---|
| SPY | 754.37 | 764.43 → **−1.3% (below)** | 731.92 → +3.1% (above) | 732.71–775.64 → **50.5% (mid)** |

SPY is 3.5% off its 52-week high (781.62), below the 50-DMA but holding above the 200-DMA, sitting mid-range after a −4.2% single-day flush on 2026-11-05 and an incomplete V-recovery that stalled Friday. QQQ and SOXX quotes were denied by the data plan, so this is an **SPY-only** read rather than the skill's full three-index gate.

**What this does to the book:** longs are lower-odds and must clear a higher zone bar with tighter risk; supply-zone shorts get more weight than usual. **Default entry mode for every name below is CONFIRMATION, not limit-in** — the skill only permits resting limit orders at the proximal in a GREENLIGHT regime.

**Sector tape, 2026-11-13 (one session, NASDAQ-listed average change — a snapshot, not a trend):**
Consumer Defensive +1.07% · Energy +0.45% · Financial Services +0.19% · Basic Materials −0.12% · Communication Services −0.14% · Healthcare −0.32% · Industrials −0.66% · Technology −1.12% · Utilities −1.28% · Consumer Cyclical −1.50% · Real Estate −1.83%

---

## Step 1 — The anticipatory layer found almost nothing

The pre-momentum coil scan is the point of this skill: find names *contracting* before they move. Across the eleven names screened, readiness scores were:

| Ticker | Readiness | State |
|---|---|---|
| META | 63.0 | **TIGHTENING** |
| ABBV | 56.9 | **TIGHTENING** |
| JPM | 38.7 | EXPANDED |
| GOOGL | 36.7 | EXPANDED |
| KO | 32.5 | EXPANDED |
| GE | 32.1 | EXPANDED |
| MSFT | 32.0 | EXPANDED |
| TSLA | 31.4 | EXPANDED |
| AMZN | 30.0 | EXPANDED |
| CVX | 26.7 | EXPANDED |
| XOM | 17.9 | EXPANDED |

**Nine of eleven read EXPANDED.** That is itself the finding: after the 5 November flush and the snap-back rally, volatility is elevated nearly everywhere, so the coil filter has almost nothing to grip. In this tape the engine is working off *levels*, not off contraction — which is the weaker of the two signals it is built to combine.

---

## Table 1 — Swing setups (ranked by conviction × risk/reward)

All R:R computed **to the actual stop**, not the distal line. "Dist" = distance from Friday's close to the entry.

| # | Ticker | Sector | Dir | Entry (proximal) | Stop | T1 | T2 | R:R | Odds /9 | Coil | Tier | Dist | Trigger + regime | Zone logic |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | Technology | Long | 497.93 | 490.55 | 559.15 | NA | **8.30** | 8 | 32 EXPANDED | **A** | −4.95% | Confirmation: tag 497.93, reclaim close on expanding volume | Fresh daily DBR demand, 1st return, sitting *above* two live weekly demand zones (393.82 core 7, 373.49 core 6) in an intact weekly uptrend — the only name where daily and weekly agree |
| 2 | **XOM** | Energy | Long | 154.84 | 151.20 | 177.46 | 183.29 | **6.21** | 8 | 18 EXPANDED | **B+** | −9.23% | Confirmation | Fresh DBR demand off the July base; T1/T2 are *real opposing supply zones*, not swing estimates. Weekly supply 181.86–188.50 caps the move |
| 3 | **GE** | Industrials | Short | 345.95 | 357.43 | 301.13 | 295.97 | **3.90** | 6 | 32 EXPANDED | **B** | +4.26% | Confirmation: tag 345.95, reject with a close back below | Fresh RBD supply from the late-August breakdown; price is *inside* a live weekly supply band (307.78–342.73), so the daily short is with the higher timeframe. T1 is a real demand zone |
| 4 | **META** | Comm. Services | Short | 694.25 | 715.12 | 593.25 | NA | **4.84** | 6 | **63 TIGHTENING** | **C** | +8.19% | Confirmation only | Best coil in the book + fresh DBD supply from the October breakdown. **Conflict:** price is also inside a live *weekly demand* zone (665.75–609.74, core 6) — shorting at 694 means selling a name that may be basing. Downgraded for that |
| 5 | **XOM** | Energy | Short | 177.46 | 180.58 | 154.84 | NA | **7.25** | 6 | 18 EXPANDED | **B** | +4.03% | Confirmation | The mirror of idea #2 — the DBD supply that caps the rally. Listed because the regime favours supply; do not hold both sides |
| 6 | **CVX** | Energy | Long | 189.23 | 185.53 | 224.71 | 231.70 | **9.59** | 7 | 27 EXPANDED | **B** | **−13.94%** | Confirmation | Clean fresh DBR demand with a real opposing supply at 224.71. Too far below spot to be actionable this week — a calendar level, not a trade |
| 7 | **TSLA** | Consumer Cyclical | Long | 358.22 | 346.54 | 414.23 | NA | **4.80** | 7 | 31 EXPANDED | **C** | −8.20% | Confirmation only | Fresh DBR demand off the 5 Nov low. **Conflict:** price (390.22) is inside a live weekly *supply* band 383.83–410.85, and T1 at 414.23 sits above it — the long is fighting the higher timeframe |
| 8 | **JPM** | Financial | Short | 347.89 | 355.16 | 325.07 | NA | **3.14** | 6 | 39 EXPANDED | **C** | **+0.49%** | **Arrival is now** — confirmation: reject 347.89 and close back below | DBD supply from the 4–5 Nov breakdown; 2nd return, so resting orders are partly consumed. R:R only just clears the 3:1 gate. The one idea where price is already at the level |
| 9 | **KO** | Consumer Defensive | Long | 88.05 | 87.32 | 99.30 | NA | `UNVERIFIED` | 6 | 33 EXPANDED | flagged | −11.28% | Watch only | Raw R:R computes to 15.4 — above the skill's implausibility threshold, and the artifact is obvious: T1 (99.30) is essentially Friday's close (99.25), so the "reward" is already realised. KO is breaking to new highs with **no overhead supply zone at all**; the honest read is momentum continuation, and 88.05 is where you'd want to buy a pullback, not a live setup |

### Sector coverage of Table 1

| Sector | Covered? | Name(s) |
|---|---|---|
| Technology | ✅ | MSFT |
| Energy | ✅ | XOM (both directions), CVX |
| Industrials | ✅ | GE |
| Communication Services | ✅ | META (GOOGL cut) |
| Consumer Cyclical | ⚠️ marginal | TSLA (C-tier; AMZN cut) |
| Financial | ⚠️ marginal | JPM (C-tier) |
| Consumer Defensive | ⚠️ watch only | KO (flagged) |
| Healthcare | ⚠️ watch only | ABBV — see below |
| **Real Estate** | ❌ **NA** | no ticker accessible |
| **Utilities** | ❌ **NA** | no ticker accessible |
| **Basic Materials** | ❌ **NA** | no ticker accessible |

### Healthcare — ABBV: a real coil with no tradeable zone

ABBV (295.03) has the second-highest readiness in the book (**56.9, TIGHTENING**), sits two points under its all-time high (302.93, set 5 Nov), has **no overhead supply zone**, and is backed by a weekly RBR demand zone scoring **8/9 (High)** at 227.73–215.37. Next earnings 2027-02-03, so the window is clean.

It is **not** in Table 1 because there is no gated zone anywhere near price: the daily demand zone scores 4/9 (fails the ≥6 gate) and the high-quality weekly zone is 22.8% below spot. Manufacturing an entry here would be exactly what this skill exists to prevent.

**How to trade it if you want to:** the trigger is a breakout and hold above **302.93** on expanding volume, with the coil as the tailwind. The defensible pullback level is the weekly proximal at **227.73** (stop 214.13, T1 302.93, R:R 5.53, core 8/9) — a position-sized level, not a swing entry.

---

## Table 2 — Off-the-radar discovery (3–5 year): **EMPTY**

No names. This is not a screening result — the task is impossible with the data on hand. The off-the-radar definition requires a $300M–$8B market cap with ≤12 covering analysts, and the FMP plan on this session serves price history for roughly a dozen mega-caps only. Every small- and mid-cap probe was denied. Reporting an empty table is the correct output; see the refresh note in the footer.

---

## "Why might this be wrong?" — one line per idea

- **MSFT** — the 497.93 zone was built during the post-earnings run; if the AI-capex narrative that drove that run cracks, the zone is a shelf of trapped longs rather than resting demand.
- **XOM (long)** — crude's November strength is doing the work here, and the zone is 9% away, so the level may only be reached on an oil breakdown that invalidates the reason to own it.
- **GE (short)** — GE rallied 20% off the 23 October low in three weeks; a supply zone that fresh in a name with that much momentum is as likely to be absorbed as respected.
- **META (short)** — price is inside a weekly demand zone, so an 8% rally into 694 would itself be evidence the base is working, and the short would be selling strength.
- **XOM (short)** — this is a counter-trend short in a name up 44% over twelve months; the weekly structure is still up.
- **CVX (long)** — 14% below spot means the market has to change its mind entirely before this fills, and by then the T1 at 224.71 will likely be stale.
- **TSLA (long)** — T1 sits above a live weekly supply band, so the trade needs the higher timeframe to break before it pays, which is not what the setup is predicated on.
- **JPM (short)** — 2nd return into the zone with R:R 3.14 leaves no margin; one wide bar through 355 and the trade is a loss with nothing recovered.
- **KO (long)** — a name at all-time highs with no overhead supply can keep going for months, so waiting 11% below for a "clean" entry is likely to mean not participating at all.
- **ABBV (watch)** — a tight coil near a high is just as capable of resolving down, and the readiness score ranks the probability of *a move*, not its direction.

---

## Footer

### Names cut in validation (signal, not filler)

| Ticker | Sector | Reason |
|---|---|---|
| GOOGL | Comm. Services | **No live zone of any kind.** Gapped −12.7% on 2026-10-29 and broke its weekly RBR demand at 344.40; every detected zone is invalidated |
| AMZN | Consumer Cyclical | Only zone is an RBD supply at 264.82–271.49 scoring **5/9** — fails the ≥6 gate; price is also *inside* the zone, so it is on neither side |
| ABBV (daily) | Healthcare | Daily DBR demand scores **4/9** — fails the gate. Moved to the watch note above on weekly structure |
| CVX (supply) | Energy | DBD supply 224.71 scores **5/9** — fails the gate |
| GE (demand) | Industrials | RBR demand 301.13 scores **5/9** — fails the gate |
| META (demand) | Comm. Services | RBR demand 578.02 → T1 606.73 gives **R:R 2.94** — fails the ≥3:1 gate |
| NVDA | Technology | **Earnings 2026-11-17** — inside the 5-trading-day buffer |
| DIS | Comm. Services | **Earnings 2026-11-17** — inside the buffer |
| WMT / TGT | Consumer Defensive / Cyclical | **Earnings 2026-11-19 / 11-18** — inside the buffer (and not accessible on this plan) |
| AAPL | Technology | Accessible but not scanned — MSFT already covers the sector and the price-history budget was spent on uncovered sectors |

### Earnings-buffer verification (all survivors clear)

MSFT 2027-01-27 · XOM 2027-01-29 · CVX 2027-01-29 · GE 2027-01-21 · META 2027-01-27 · TSLA 2027-01-27 · JPM 2027-01-14 · KO 2027-02-09 · ABBV 2027-02-03. No survivor reports inside the trade window.

### Data integrity and what to refresh

- **ONE-SOURCE on every level.** The Step-3 cross-feed check could not run: `query1/query2.finance.yahoo.com`, `stooq.com` and `quote.cnbc.com` all fail DNS/CONNECT under this session's network policy. A level backed by one feed is exactly the silent-bad-data risk that check exists to catch. **Verify each level on TradingView before order entry.**
- **Three sectors unscreened.** Real Estate, Utilities and Basic Materials returned `ACCESS DENIED — requires a higher plan` for every ticker tried. To close this gap, either upgrade the FMP plan to one covering the full US universe, or allow `query1.finance.yahoo.com` / `stooq.com` in the session's network settings so the skill's own keyless fetchers work again.
- **Detection standard loosened** from `--leg-mult 1.6` to `1.0` with `--max-base 8` over 90 bars, because the default produced no live zones on nine of eleven names. Scores in Table 1 are therefore generous relative to the skill's documented bar.
- **Big Picture / Arrival / Curve enhancers are first-pass.** They need visual confirmation on a chart; the weekly conflicts flagged on META and TSLA are the ones I could verify mechanically.
- Zone workbooks (one row per zone, every enhancer column) are in `reports/zones/*_zones_2026-11-13.xlsx`.

### Overall confidence: **0.40**

Driven down by: single unverified feed, a loosened detection standard, three of eleven sectors unscreenable, and an anticipatory layer that found two tightening names out of eleven. The two things I would actually act on from this sheet are **MSFT at 497.93** (the only setup where daily and weekly agree and the core score clears 8) and **JPM at 347.89** (the only one where price has already arrived, accepting that R:R 3.14 leaves no margin).

*Not financial advice. Position sizing and the trade decision are yours.*
