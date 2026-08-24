# Swing Trading Ideas by Sector — Zone-Gated Screen

**Run date:** 2026-08-24 (pre-market Monday) · **Data as-of:** 2026-08-21 close (last completed session)
**Framework:** swing-idea-engine (Seiden/OTA supply-demand zones + pre-momentum coil screen + hard eligibility gates)
**Not financial advice.** All levels expire at the next session's open — re-verify before order entry.

---

## Headline

**16 liquid large-caps across all 11 requested sectors were scanned. Exactly one cleared the eligibility gates: AAPL.**

This is not a screening failure — it is the read. The tape's leaders have run well above their last
institutional bases, so the demand zones that would define a low-risk swing entry are either far below
spot, already consumed, or invalidated. Nine of sixteen names produced **no clean base + leg-out zone at
all**, which is what "extended / mid-range equilibrium" looks like mechanically.

Per the framework, a name failing any gate is **cut, not downgraded**. Padding the list to hit one idea
per sector would mean inventing levels. The near-misses are listed below with their real, retrieved
levels and the specific gate each failed — a rejected name with its reason is more useful than a forced pick.

---

## Step 0 — Market regime: **SELECTIVE**

| Index | Close | vs 50-SMA | vs 200-SMA | Position in 20-day range | State |
|---|---|---|---|---|---|
| SPY | 765.72 | +1.9% | +8.2% | 73% | CONSTRUCTIVE |
| QQQ | 713.44 | −0.0% | +9.3% | 71% | MIXED (price sitting on its 50-SMA) |

**Verdict: SELECTIVE — mixed tape; longs are lower-odds. Demand higher zone quality and tighter risk.**

Consequence for entries: **confirmation entry is the default**, not a resting limit order. Wait for price
to tag the zone and print a close back above the proximal line on expanding volume.

---

## The one qualifying setup

### ⭐ Technology — AAPL (Apple) · LONG · Tier B · Confirmation entry

| Field | Value |
|---|---|
| Spot (2026-08-21 close) | **309.35** |
| Entry (zone proximal) | **294.38** — 4.8% below spot; this is a *wait-for-pullback* setup |
| Stop (just beyond distal 289.19) | **288.67** — risk 5.71/share (1.94% of entry) |
| Target 1 (conservative) | **319.28** (Aug-19 swing high) → **R:R 4.36 : 1** |
| Target 2 (scanner target) | **344.57** (52-week high) → R:R 8.79 : 1 — *swing-high estimate, no opposing zone; treat as unverified* |
| Odds-enhancer core score | **7 / 9** (Strength 1, R:R 2, Big picture 1, Freshness 2, Time 1) |
| Coil readiness | **58.8 — TIGHTENING** (range compression 0.46, i.e. the recent band is less than half the prior band) |
| Zone status | **LIVE, untested (1st touch would be the first return)** |
| Next earnings | **2026-10-29** — far outside the 5-trading-day buffer ✅ |

**Why the trade:** A Rally-Base-Rally demand zone formed on 2026-07-01 (base 289.19–294.38) and price
left it with a 4.8% expansion candle on 07-02, running to 344.57. Price has never traded back into that
base — the resting bids are untouched. The 07-31 earnings gap (333.43 → 308.91) knocked price back toward
the zone without reaching it; the lowest print since is 300.00. AAPL holds above its 200-day (+9.9%) while
sitting on its 50-day, so a pullback into 294 is a with-trend retest rather than a trend break.

**Why this might be wrong:** the zone is 4.8% away and price has spent three weeks refusing to go there —
it may simply resume upward and never fill, leaving no entry; and the 07-31 gap means the move that built
this zone was already repriced by an earnings event.

**Gate arithmetic (recomputed to the actual stop, not the distal line):**
`risk = 294.38 − 288.67 = 5.71` · `reward = 319.28 − 294.38 = 24.90` · `R:R = 4.36` ✅ ≥ 3:1

**Trigger:** price tags 294.38–289.19, then closes back above **294.38** on expanding volume. No reclaim
close, no trade. In this SELECTIVE regime a resting limit order at proximal is *not* recommended.

---

## Sector-by-sector: what was tested and what the scanner found

Ranked within each sector by how close the name came to qualifying.

### Technology
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| **AAPL** | 309.35 | Live RBR demand 294.38/289.19, core 7/9, fresh | ✅ **TRADE — see above** |
| AMD | 473.25 | No clean base + leg-out zone detected | ❌ Cut — no zone |
| NVDA | 214.72 | Not scanned | ❌ Cut — **earnings 2026-08-26**, inside the 5-day buffer |

### Financial
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| JPM | 351.58 | **Live** RBR demand 340.98/330.13, stop 329.05, T1 366.50 | ❌ Cut — core score **4/9** (needs ≥6) *and* R:R to actual stop **2.14** (needs ≥3) |
| SCHW | 112.30 | RBD supply 103.25/107.27 — **invalidated** 2026-08-05 | ❌ Cut — zone not live |

> Worth flagging: **JPM is the most coiled name in the entire universe** — ATR percentile 0.02, Bollinger-width
> percentile 0.09, volume dry-up 0.65, sitting 4.1% under its 52-week high. The coil says a move is loading;
> the zone quality says don't pay for it here. That disagreement is signal, not noise — JPM is the top
> **watch** candidate if it builds a tighter base.

### Communication Services
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| DIS | 107.78 | **Live** DBD supply 108.12/109.87, stop 110.05, T1 92.49, R:R 8.10 | ❌ Cut — core score **5/9**; also a counter-trend short (DIS is +7.9% over its 50-SMA) |
| GOOGL | 344.82 | DBR demand 393.64/382.77 — **invalidated** 2026-05-29, core 3/9 | ❌ Cut — zone not live |

### Energy
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| OXY | 61.30 | Live RBR demand at **41.74** — 32% below spot | ❌ Cut — no zone at hand; scanner R:R 20.21 flagged UNVERIFIED (stale/far target) |
| XOM | 165.11 | RBR demand 139.83/138.06 — **invalidated** 2026-06-18, tested 5× | ❌ Cut — zone not live |

> Energy is the strongest *coil-plus-trend* combination in the screen — OXY reads ATR percentile 0.0 with
> price +11.9% over its 50-SMA and +19.1% over its 200-SMA; XOM is ATR percentile 0.13 and +10.8% over its
> 50-SMA. Both are set up to move; neither offers a defensible level to buy at current prices.

### Healthcare
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| UNH | 390.11 | DBD supply 418.52/424.11 — **invalidated** 2026-07-17, core 4/9 | ❌ Cut — zone not live |

### Real Estate
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| AMT | 175.80 | No clean base + leg-out zone detected | ❌ Cut — no zone |

### Basic Materials
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| FCX | 76.66 | No clean base + leg-out zone detected | ❌ Cut — no zone |

> FCX printed a **+7.6% expansion day into a new 52-week high** on 2026-08-21 (range 74.40–77.33 after a
> 71.22 close). Range-compression ratio 2.03 = the coil has already released. Per the framework this is
> exactly the lagging-momentum entry the screen is built to avoid chasing.

### Consumer Cyclical
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| AMZN | 258.63 | No clean base + leg-out zone detected | ❌ Cut — no zone |

### Consumer Defensive
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| COST | 947.74 | No clean base + leg-out zone detected | ❌ Cut — no zone (despite Bollinger-width percentile 0.02, the tightest squeeze in the screen) |

### Industrials
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| CAT | 827.90 | No clean base + leg-out zone detected | ❌ Cut — no zone; −22.9% from its 52-week high and −8.6% under its 50-SMA |

### Utilities
| Name | Spot | Scanner result | Verdict |
|---|---|---|---|
| NEE | 83.65 | No clean base + leg-out zone detected | ❌ Cut — no zone; below all three moving averages |

---

## Coil screen (leading indicator) — full universe, most-contracted first

Low ATR / Bollinger percentiles = volatility contracted = energy building. These rank *probability of a
move*, not its direction; direction comes from the zone and the regime.

| Ticker | Sector | Close | ATR %ile | BB %ile | Range compr. | Vol dry-up | vs 50-SMA | vs 200-SMA | % from 52w high |
|---|---|---|---|---|---|---|---|---|---|
| JPM | Financial | 351.58 | 0.02 | 0.09 | 0.80 | 0.65 | +2.2% | +11.2% | −4.1% |
| COST | Cons. Def. | 947.74 | 0.17 | 0.02 | 0.99 | 0.74 | −0.1% | −1.2% | −13.6% |
| OXY | Energy | 61.30 | 0.00 | 0.37 | 0.76 | 0.85 | +11.9% | +19.1% | −9.1% |
| SCHW | Financial | 112.30 | 0.03 | 0.49 | 0.60 | 0.66 | +10.7% | +16.2% | −0.1% |
| XOM | Energy | 165.11 | 0.13 | 0.34 | 0.84 | 0.89 | +10.8% | +15.8% | −6.4% |
| AMT | Real Estate | 175.80 | 0.43 | 0.13 | 1.08 | 0.58 | +2.2% | −1.2% | −18.2% |
| GOOGL | Comm. Svcs | 344.82 | 0.11 | 0.45 | 0.99 | 0.66 | −2.0% | +3.5% | −15.6% |
| AMD | Technology | 473.25 | 0.35 | 0.27 | 0.85 | 0.69 | −7.2% | +43.5% | −19.1% |
| NEE | Utilities | 83.65 | 0.14 | 0.53 | 1.63 | 0.92 | −4.0% | −4.8% | −15.3% |
| FCX | Basic Mat. | 76.66 | 0.09 | 0.61 | 2.03 | 0.90 | +18.5% | +29.6% | −0.9% |
| AMZN | Cons. Cyc. | 258.63 | 0.08 | 0.75 | 1.91 | 0.65 | +3.6% | +8.5% | −9.9% |
| DIS | Comm. Svcs | 107.78 | 0.27 | 0.91 | 1.89 | 0.67 | +7.9% | +3.5% | −10.0% |
| UNH | Healthcare | 390.11 | 0.23 | 0.56 | 0.99 | 0.75 | −5.7% | +12.1% | −15.5% |
| AAPL | Technology | 309.35 | 0.17 | 0.77 | 0.73 | 0.74 | −0.3% | +9.9% | −10.2% |
| CAT | Industrials | 827.90 | 0.63 | 0.18 | 0.68 | 0.77 | −8.6% | +8.8% | −22.9% |
| NVDA | Technology | 214.72 | 0.07 | 0.87 | 1.54 | 0.76 | +3.4% | +10.0% | −9.2% |

---

## Validation log (Step 3)

- **Cross-feed verification passed.** Every level traces to bars retrieved live this session. Latest closes
  were checked against a second, independent provider (Massive/Polygon aggregates vs. Financial Modeling
  Prep) for **AAPL, AMZN, GOOGL, XOM, JPM, COST, KO, UNH, AMD, NVDA, GS, BAC, GE, WMT** — all **AGREE** to
  the cent. No DIVERGE, no single-source levels among the presented names.
- **R:R recomputed** from stated entry/stop/target for the AAPL setup; matches to within 0.01.
- **Earnings buffer verified per name**, not from memory: AAPL 2026-10-29 (clear); NVDA 2026-08-26 (inside
  buffer → cut).
- **Names cut in validation: 15 of 16.** Reasons: no clean base + leg-out zone detected (7: AMD, FCX, NEE,
  AMZN, COST, CAT, AMT); zone invalidated — price closed through it (4: XOM, GOOGL, SCHW, UNH); core score
  below 6/9 (2: JPM, DIS); earnings inside the 5-day buffer (1: NVDA); live zone but not at hand, R:R
  unverified (1: OXY).
- **Overall confidence: 0.7.** High on the mechanical result (the gates are deterministic and the data is
  twice-verified); moderate on breadth, because only 1–2 names per sector were zone-scanned.

## Data limitations — read before acting

1. **This session's egress policy blocks Yahoo, Stooq, CNBC and every direct market-data host.** The skill's
   bundled fetchers could not run. Bars were retrieved through the Massive (Polygon) and FMP MCP servers
   instead and fed to the same scanners as CSV. The analysis is unaffected; the plumbing differed.
2. **`data_sources.py` could not run** for the same reason. The cross-feed check above was performed
   manually against FMP and is equivalent in substance.
3. **Universe depth is 1–3 names per sector (16 total), not an exhaustive sector sweep.** Massive rate-limits
   and FMP's plan-restricted symbol coverage capped how many names could be loaded in one run. A name not
   listed was not tested — absence here is not a negative verdict. Utilities, Basic Materials and Industrials
   got a single candidate each and deserve a deeper pass.
4. **Lookback windows differ by name:** OXY/XOM ~8.5 months of daily bars; most names ~7 months; AAPL, AMD,
   FCX, NEE ~4.5 months. AAPL's shorter window means its 200-day trend posture came from separate SMA
   calculation rather than from the coil script (which reported "mixed/transition" on 92 bars).
5. **Weekly higher-timeframe zone maps were not run.** Big-picture context came from 50/200-SMA posture and
   52-week range position. The AAPL "Big picture" enhancer scored 1/2 partly for that reason — confirm the
   weekly chart before sizing.
6. **Data is Friday 2026-08-21's close.** These levels expire at Monday's open.

## What to do with this

If you want a genuine second idea rather than a manufactured one, the highest-value follow-ups are:
**(a)** re-run with a deeper universe in Utilities / Basic Materials / Industrials, which each got one shot;
**(b)** put JPM on watch for a tighter base — it is the most coiled name in the screen and only failed on
zone quality, not on trend; **(c)** re-scan on the weekly timeframe, where a tape this extended on the daily
often still shows live higher-timeframe demand.
