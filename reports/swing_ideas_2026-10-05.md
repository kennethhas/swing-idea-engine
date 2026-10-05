# Swing Trading Ideas — 11 Sectors
**Generated:** 2026-10-05 (pre-open Monday) · **Data as-of close:** 2026-10-02
**Method:** `swing-idea-engine` skill (Regime → Coil → Level → Trigger), zone scanner run on live bars
**Not financial advice. All levels expire at the next session's open — re-verify before order entry.**

---

## ⚠️ Read this first: two material data caveats

1. **The repo had no market data.** `swing-idea-engine` ships scripts but no cached
   prices, and `claude-trading-skills/reports/` is empty. The skill's own feed (Yahoo)
   is **blocked by this session's egress policy** (403 on CONNECT). Every number below
   was retrieved live this session from **Massive/Polygon** via MCP.
2. **No cross-feed verification was possible → every level is SINGLE-SOURCE.** The
   skill's Step-3 `data_sources.py` check (Yahoo vs CNBC) could not run: Yahoo and all
   direct feeds are policy-blocked, FMP's `chart`/`quote`/`news` endpoints are gated by
   the account's plan tier, and Bigdata.com credits are exhausted. Per the skill's own
   rule these levels are **ONE-SOURCE: keep but verify manually** on TradingView before
   risking capital. This is the silent-bad-data risk the check exists to catch.

---

## STEP 0 — Regime: GREENLIGHT on the index, but breadth is the story

| Index | Close | SMA50 | SMA200 | vs SMA200 | 20d range loc | Posture |
|---|---|---|---|---|---|---|
| SPY | 769.64 | 763.70 | 720.47 | +6.8% | 0.78 | CONSTRUCTIVE |
| QQQ | 749.58 | 716.82 | 668.60 | +12.1% | 0.91 | CONSTRUCTIVE, **extended** |

Price > SMA50 > SMA200 on both → demand-zone longs are with-regime. **But the sector
tape contradicts the index.** Measured sector-ETF returns:

| Sector | ETF | 1m | 3m | 6m |
|---|---|---|---|---|
| Energy | XLE | −3.5% | **+18.0%** | +6.0% |
| Technology | XLK | **+8.8%** | **+10.6%** | **+46.9%** |
| *S&P 500* | *SPY* | *+0.6%* | *+3.3%* | *+17.4%* |
| Healthcare | XLV | −3.9% | +1.5% | +13.2% |
| Comm Svcs | XLC | −1.9% | +0.7% | −1.2% |
| Financial | XLF | −7.2% | −3.8% | +8.0% |
| Cons Defensive | XLP | −5.9% | −5.3% | −1.7% |
| Cons Cyclical | XLY | −4.2% | −6.1% | +1.8% |
| Basic Materials | XLB | −7.7% | −6.1% | −3.1% |
| Industrials | XLI | −1.6% | −7.6% | +3.8% |
| Real Estate | XLRE | −6.7% | −8.7% | −1.9% |
| Utilities | XLU | −6.7% | −13.0% | −14.1% |

**Only Technology is positive over 1 month. 9 of 11 sectors are negative.** The index is
being carried by a narrow group. Effective posture: **SELECTIVE, not GREENLIGHT** —
demand higher zone quality and tighter risk, and treat ideas in the bottom six sectors as
counter-trend regardless of how good the R:R screens.

---

## STEP 1/2 — What survived the gates

27 liquid names (price > $10, > $80M/day dollar volume) across all 11 sectors were run
through the coil scan and the Seiden/OTA zone scanner on daily (1y **and** 6-month
windows, per the skill's parabolic-name rule) plus weekly for higher-timeframe context.

**Exactly one name clears every eligibility gate** (core odds ≥ 6/9, R:R-to-actual-stop
≥ 3:1, zone live, correct side of price, no earnings inside 5 trading days).

That is the honest result, and it is consistent with the breadth data above: in a tape
where nine sectors are rolling over, clean with-trend demand zones are scarce. Everything
in Table 2 is a **measured level map, not a gated setup** — labelled as such.

### TABLE 1 — Zone-gated setup (1 name)

| Ticker | Sector | Entry (proximal) | Stop (beyond distal) | T1 | T2 | R:R | Odds | Coil | Tier | Trigger | Zone logic |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **CRM** | Technology | **209.17** | **197.93** | **253.62** | 268.27 | **3.95:1** | **8/9** | 76.5 COILED | **B** | Confirmation: daily close reclaiming 209.17 on expanding volume | Daily RBR demand 209.17/198.95, freshness 2 (untested/1st return), scanner confidence High. T1 capped at the **weekly RBD supply proximal 253.62** (core 8/9) — not the 268.27 swing high, because that weekly supply is the real overhead obstacle |

- **Entry sits 5.8% below spot (234.69).** This is a resting-limit / wait level, not an
  at-market idea. Nothing to do today but set the alert.
- **Why might this be wrong?** Price is wedged between its own daily demand at 209 and
  weekly supply at 253.62, so the 3.95:1 depends entirely on price reaching that weekly
  supply rather than stalling mid-range — and a daily long under weekly supply overhead is
  the setup the skill normally cuts.
- Tier B not A: core score 8/9 qualifies for A, but R:R 3.95:1 is just under the 4:1 A threshold.

### TABLE 2 — Per-sector level map (NOT zone-gated; ranked by conviction)

Rules are fixed so every number is reproducible from the retrieved bars:
**PULLBACK** (position in 20d range < 0.60): entry = max(20d low, SMA50) below spot,
stop = entry − 1.5×ATR14, T1 = 20d high, T2 = 60d high.
**BREAKOUT** (≥ 0.60): entry = 20d high, stop = entry − 2.0×ATR14, T1 = 60d high, else 126d high.
Coil = skill's 0–100 readiness (COILED ≥70, TIGHTENING 55–69, EXPANDED <40).

#### ⭐ Technology — the only with-regime sector (XLK +8.8% 1m)
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **CRM** | 234.69 | Pullback | 221.18 | 209.30 | 263.60 | 268.27 | 2.92:1 | 5.4% | 76.5 COILED | UPTREND | See Table 1 — the gated version (209.17 entry) is the better structure |
| NVDA | 233.95 | Breakout | 237.88 | 227.58 | **NA** | NA | **NA** | 4.3% | 83.2 COILED | UPTREND | Coiled at all-time high, +7.2% over SMA50. **T1 = NA: no overhead level exists**, so R:R is unmeasurable — a valid NA, not a free trade |
| AVGO | 355.14 | Pullback | 335.81 | 320.87 | 372.70 | 432.73 | 2.47:1 | 4.5% | 82.0 COILED | **DOWNTREND** | Coiled, but below SMA50 *and* SMA200 and 28% off its 495.00 high. Weekly demand zone at 327.25 scored 6/9 but **failed R:R at 2.49:1** → cut |

#### Energy — strongest 3m (XLE +18.0%), now pulling back
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **CVX** | 206.69 | Pullback | 202.55 | 196.30 | 217.78 | NA | 2.43:1 | 3.1% | 77.8 COILED | UPTREND | Clean px>SMA50>SMA200, coiled into its SMA50. Daily demand zone exists at 152.41 (core 6/9) but is **26% below spot with a 21.5:1 R:R → flagged UNVERIFIED artifact and cut**. ⚠️ Earnings **Oct 30** |
| XOM | 164.01 | Pullback | 160.54 | 155.16 | 169.64 | NA | 1.69:1 | 3.4% | 80.4 COILED | UPTREND | Coiled, with-trend, but spot is already 59% up its 20d range so the move to T1 is small → R:R fails. ⚠️ Earnings **Oct 30** |
| DVN | 47.65 | Pullback | 46.93 | 44.58 | 51.70 | NA | 2.03:1 | 5.0% | 60.2 TIGHTENING | UPTREND | Third Energy name; weakest coil and widest risk of the three |

#### Healthcare — modestly positive 3m
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **IQV** | 258.21 | Pullback | 253.80 | 243.53 | 277.40 | NA | 2.30:1 | 4.1% | 73.4 COILED | UPTREND | Best trend in the sector (+24.7% 3m, +49.0% 6m), coiled at 23% of its 20d range — textbook pullback-in-uptrend. Two daily demand zones found but both scored ≤6/9 with the nearest 34% below spot → cut |
| MRK | 144.30 | Pullback | 142.32 | 137.46 | 153.57 | 156.92 | 2.31:1 | 3.4% | 72.2 COILED | UPTREND | Coiled at 18% of 20d range, px>SMA50>SMA200. Scanner's 8/9 demand zone sits at 78.76 — **45% below spot**, an old base, not tradeable → cut |

#### Industrials — weak sector (−7.6% 3m) but two names in real uptrends
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **DE** | 687.00 | Pullback | 649.02 | 624.30 | 721.22 | NA | **2.92:1** | 3.8% | 59.0 TIGHTENING | UPTREND | Best R:R among trend-aligned names outside CRM. Clean px>SMA50>SMA200, +10.6% 3m against a −7.6% sector = genuine relative strength |
| ETN | 436.11 | Breakout | 452.00 | 426.14 | 478.00 | NA | 1.01:1 | 5.7% | 71.2 COILED | UPTREND | Coiled and with-trend, but entry is 3.6% above spot and T1 only 5.8% beyond → **R:R 1.01:1, structurally not worth taking** |

#### Basic Materials
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **FCX** | 72.04 | Pullback | 70.54 | 66.91 | 78.64 | 80.24 | 2.23:1 | 5.2% | **86.2 COILED** | UPTREND | Second-highest coil in the whole scan and with-trend (px>SMA50>SMA200, +18.2% 3m) — the tightest "about to move" reading in a weak sector |
| NEM | 115.56 | Pullback | 113.86 | 108.31 | 130.48 | 135.29 | **2.99:1** | 4.9% | 66.6 TIGHTENING | MIXED | Highest R:R in the sector and just under the 3:1 gate, but px is below SMA50 and only 10% up its 20d range — falling, not coiling |

#### Consumer Defensive
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **TGT** | 156.00 | Pullback | 155.68 | 150.36 | 164.82 | 170.75 | 1.72:1 | 3.4% | **88.0 COILED** | UPTREND | **Highest readiness of all 27 names** and the sector's clear leader (+19.8% 3m, +29.5% 6m vs XLP −5.3%). Sitting right on its SMA50 at 22% of the 20d range. Its daily demand zone 155.69/150.32 scored only **4/9 — tested 6×, orders consumed** → cut. Watch, don't buy the level |
| PM | 187.46 | Pullback | 181.01 | 174.72 | 195.49 | 207.76 | 2.30:1 | 3.5% | 78.1 COILED | MIXED | Coiled but px is inside a **weekly supply zone (183.40/191.30, core 6/9)** — price sits *inside* the zone, so it fails the side-of-price gate in both directions |

#### Communication Services
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **GOOGL** | 343.50 | Pullback | 327.74 | 313.99 | 364.17 | 384.48 | 2.65:1 | 4.2% | 61.7 TIGHTENING | MIXED | Tightening right at its SMA50 (343.50 vs 344.37) after a −4.6% 3m digestion of a +16.1% 6m run. ⚠️ Earnings **Oct 28** — inside any multi-week hold |
| META | 728.08 | Breakout | 779.82 | 722.06 | NA | NA | NA | 7.4% | **29.1 EXPANDED** | UPTREND | +22.8% in a month, +16.5% over SMA50 — **coil already released, this is the chase**. Weekly DBD supply 713.01/742.41 scored 7/9 but **price is inside it** → fails side-of-price. ⚠️ Earnings Oct 28 |

#### Financial
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **MET** | 94.43 | Pullback | 92.21 | 89.40 | 99.13 | 100.93 | 2.47:1 | 3.0% | 57.0 TIGHTENING | MIXED | Tightest risk in the table (3.0%) and +33.5% 6m, but below SMA50 in a −3.8% sector |
| PYPL | 52.80 | Pullback | 50.80 | 48.71 | 56.14 | 62.73 | 2.56:1 | 4.1% | 73.3 COILED | MIXED | Coiled and sector leader on 3m (+16.1%), but −6.6% below SMA50 and barely over SMA200 (50.25). ⚠️ Earnings **Oct 27** |

#### Consumer Cyclical
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **ULTA** | 543.69 | Pullback | 534.56 | 512.25 | 566.87 | NA | 1.45:1 | 4.2% | 86.4 COILED | MIXED | Very tightly coiled and above SMA50, but **below SMA200 (555.67)** and T1 is only 4.3% away → R:R 1.45:1 |
| ABNB | 162.43 | Pullback | 149.00 | 140.99 | 184.51 | 193.45 | **4.43:1** | 5.4% | **34.7 EXPANDED** | MIXED | **Highest R:R in the whole sweep — and a trap.** The 4.43:1 comes from a 20d range so wide (149.00–184.51) that the name is clearly *expanding downward*, not coiling. Below SMA50, EXPANDED. High R:R here is distance, not edge |

#### Real Estate — second-worst sector
| Ticker | Px | Plan | Entry | Stop | T1 | T2 | R:R | Risk | Coil | Posture | Reason / caution |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **EQIX** | 1025.72 | Pullback | 987.79 | 951.65 | 1066.51 | 1109.22 | 2.18:1 | 3.7% | 56.9 TIGHTENING | MIXED | Best relative strength in a −8.7% sector (+2.4% 3m) and holding SMA200 (987.51) — the entry and the SMA200 coincide, which is the one thing to like here |
| DLR | 178.55 | Pullback | 172.83 | 166.68 | 192.09 | 207.47 | **3.13:1** | 3.6% | 58.2 TIGHTENING | **DOWNTREND** | Clears 3:1 on paper but is below SMA50 *and* SMA200 in the second-worst sector. Counter-regime |

#### Utilities — no idea offered
Worst sector on every horizon (−6.7% 1m, −13.0% 3m, −14.1% 6m). **All three candidates
are below both their SMA50 and SMA200** — there is no with-trend long here, and the two
that clear 3:1 (CEG 3.90:1, VST 3.22:1) do so only because they have fallen far enough to
leave a lot of air to their 60-day highs. That is distance, not edge.

| Ticker | Px | R:R | Coil | Posture | Verdict |
|---|---|---|---|---|---|
| CEG | 257.49 | 3.90:1 | 53.0 NEUTRAL | DOWNTREND | Counter-regime. px < SMA50 (271.47) < SMA200 (287.79) |
| VST | 140.02 | 3.22:1 | 67.9 TIGHTENING | DOWNTREND | Counter-regime. Only live zone is **supply at 167.17 (core 5/9)** — i.e. the structure argues short, not long |
| AES | 14.91 | NA | 48.6 | — | **CUT — see anomaly note below** |

---

## Conviction ranking (top 10)

Ranked on: gate status → trend alignment → coil readiness → R:R. Counter-trend names are
excluded from the top tier no matter how good their R:R screens.

| # | Ticker | Sector | Why it ranks here | R:R |
|---|---|---|---|---|
| 1 | **CRM** | Technology | Only name passing every zone gate. 8/9 odds, COILED, with-trend, in the only strong sector | 3.95:1 |
| 2 | **DE** | Industrials | Best R:R among trend-aligned names; real relative strength (+10.6% vs −7.6% sector) | 2.92:1 |
| 3 | **FCX** | Materials | 86.2 coil (2nd highest) + full uptrend + leading its sector | 2.23:1 |
| 4 | **CVX** | Energy | COILED into SMA50, with-trend, in the best 3m sector | 2.43:1 |
| 5 | **IQV** | Healthcare | COILED pullback in a strong uptrend, low in its 20d range | 2.30:1 |
| 6 | **MRK** | Healthcare | COILED, with-trend, tight risk | 2.31:1 |
| 7 | **GOOGL** | Comm Svcs | Tightening exactly at SMA50 after an orderly digestion | 2.65:1 |
| 8 | **TGT** | Cons Defensive | Highest coil in the scan + strongest sector-relative trend — but R:R too thin to act | 1.72:1 |
| 9 | **EQIX** | Real Estate | Entry coincides with SMA200; best name in a bad sector | 2.18:1 |
| 10 | **MET** | Financial | Tightest risk (3.0%); strong 6m — but below SMA50 | 2.47:1 |

**Deliberately NOT ranked despite attractive R:R:** ABNB (4.43:1), CEG (3.90:1),
VST (3.22:1), DLR (3.13:1), NEM (2.99:1). Every one is below its SMA50, in a negative
sector, with its R:R inflated by how far it has already fallen.

---

## Footer — validation log (mandatory)

**Names cut in validation, with reason (19 of 27):**

| Ticker | Cut reason |
|---|---|
| AES | **Data anomaly.** ATR14 = $0.05 on a $14.91 stock (0.31%); entire 126-day range is $14.24–14.94 (4.7%); T1 sits 0.2% above spot. A 0.67% stop is inside one day's noise. Price behaviour is consistent with a **pending-acquisition pin**, which would make its "COILED" reading an artifact of a dead tape, not stored energy — exactly the false positive the skill warns about. *Inference from price only — news feeds were unavailable this session; verify before concluding.* |
| WBD | **Data anomaly.** Spot 30.94 is the 126-day high (30.97) to the penny, ATR 1.23%, yet 10d volume is **2.49× its 50d average** — range compressing while volume explodes. Consistent with an event/deal pin. Only zone scored 5/9. *Same inference caveat.* |
| META | Weekly supply 7/9 but **price inside the zone** → fails side-of-price. Coil EXPANDED (29.1) |
| PM | Weekly supply 6/9 but **price inside the zone** → fails side-of-price |
| AVGO | Weekly demand 6/9 but **R:R 2.49:1** → fails ≥3:1 |
| CVX, MRK (×2), IQV (×2) | Core score met on some zones but zone is 26–45% below spot — not at hand; CVX's 21.5:1 **flagged UNVERIFIED** per the implausible-R:R rule |
| TGT | Demand zone **tested 6× (orders consumed)**, wide 5-candle base → core 4/9 |
| PM, WBD, VST, IQV (2nd zone) | Core score 5/9 → below the 6/9 gate |
| TGT (2nd), CRM (2 supply zones), IQV (2nd) | Core 3–4/9 → below gate |
| ETN, EMR, ULTA, XOM, NVDA | No qualifying zone; mechanical R:R ≤ 1.72:1 or T1 = NA |
| CEG, VST, DLR, AVGO | Below SMA50 *and* SMA200 → counter-regime, excluded from ranking |
| ABNB, NEM, PYPL, MET, EQIX, GOOGL, ULTA | No gated zone; retained in Table 2 as level maps only |

**Earnings check (gate: nothing inside 5 trading days, i.e. before Oct 12):** PASSED for
all names. Confirmed dates inside a typical swing window: **PYPL Oct 27, GOOGL Oct 28,
META Oct 28, XOM Oct 30, CVX Oct 30.** CRM, NVDA, TGT, IQV, MRK, EQIX, FCX, NEM, MET,
ETN, DE and ULTA did not appear in the Oct 5–Nov 6 calendar pulls — but **that endpoint
returns a capped ~20-row list, so absence is not confirmation.** Verify each date before
holding past mid-October; Q3 season starts Oct 13.

**Overall confidence: 0.45.** Composed of: high confidence in the retrieved prices and in
the gate arithmetic (both reproducible); **low** confidence from the single-source feed
with no cross-check; and a genuine structural finding that the tape offers almost nothing
clean — which is information, not a failure of the screen.

**Standing reminders:** all levels expire at the next session's open · single unofficial
feed, no cross-verification possible this session · re-verify every zone on TradingView
before order entry · the coil score ranks probability of *a* move, not its direction ·
position sizing is yours · **not financial advice**.

**Suggested data refresh:** add a second price feed reachable from this environment (an
FMP plan tier that enables `chart`/`quote`, or allow-list a feed host in the egress
policy) so the skill's Step-3 cross-feed check can actually run. Caching a daily OHLCV
snapshot into the repo would also make these runs reproducible instead of rate-limited.
