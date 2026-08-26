# Data Center + Energy — Combined Zone-Gated Screen

**Run date:** 2026-08-25 · **Data as-of:** 2026-08-25 close · **Regime:** SELECTIVE
**Not financial advice.** Levels expire at the next session's open.

---

## Answer

**Energy: XOM — and it has gotten better since Monday.**
**Data center: still nothing.** I extended the search into the part where the two themes overlap — power
generation built for data centers — and it came back empty too. Fourteen names now zone-scanned across the
theme, zero qualifying.

---

## ⛽ ENERGY — XOM (ExxonMobil) · LONG · Tier A- · **the pick**

Re-verified today with two additional completed sessions. The zone is **still live and still untested**,
and three things improved:

| | Monday (08-21 data) | Today (08-25 data) |
|---|---|---|
| Spot | 165.11 | **160.64** |
| Distance to entry | −6.2% | **−3.6%** |
| Coil readiness | 59.7 TIGHTENING | **71.6 — COILED** |
| Core odds score | 8/9 | 8/9 (unchanged) |
| Zone status | live, untested | **live, untested** |

| Field | Value |
|---|---|
| Entry (zone proximal) | **154.84** |
| Stop (beyond distal 151.53) | **151.20** — risk 3.64/share, 2.35% of entry = **1.06 × ATR** |
| Target 1 | **168.64** (Aug-20 swing high) → **R:R 3.79 : 1** |
| Target 2 | **176.41** (52-week high) → R:R 5.93 : 1 |
| Odds-enhancer core | **8 / 9** — highest score found in any scan this week |
| Next earnings | **2026-10-30** ✅ calendar-verified |
| Trend | +10.8% vs 50-SMA, +15.8% vs 200-SMA |

**The zone:** price dropped into 2026-08-06/07 (base 151.53–154.84), left with a +4.4% expansion on 08-10,
and ran to 168.64. It has never come back. Lowest print since is 157.43.

**What changed this week:** price fell 165.11 → 164.05 → 160.64 on rising volume (17.5M Tuesday vs 14.3M
Friday). It is walking toward the zone, not away from it, and the contraction reading crossed from
TIGHTENING into **COILED**. That is the skill's Regime → Coil → Level sequence lining up with only the
trigger left to fire.

**Trigger (SELECTIVE regime = confirmation only):** wait for price to tag 154.84–151.53 and close back
above **154.84** on expanding volume. No reclaim close, no trade.

**Why this might be wrong:** three straight down days into a zone is exactly what a failing level looks
like before it fails. If 154.84 breaks on volume, the next live demand is all the way down at 119.80 — a
20% air pocket beneath it.

⚠️ **One caveat on the freshness:** the whole energy complex is stretched (XOM still +10.8% over its
50-day). A pullback deep enough to fill 154.84 may mean the sector move is breaking rather than resting.

---

## 🖥️ DATA CENTER — no qualifying setup, second confirmation

Monday's pass covered the hardware, networking and REIT side. Today I added the cohort that sits at the
intersection of both your themes — **power generation for data centers** — on the theory that if the
compute names were broken, the electrons behind them might not be.

They are worse.

| Ticker | Role | Close | vs 50-SMA | vs 200-SMA | % from 52w high | Zone result |
|---|---|---|---|---|---|---|
| ETR | Utility, big DC load | 106.24 | −4.5% | +1.1% | −10.3% | Live **supply** 107.34, core **4/9** → cut |
| PEG | Utility, nuclear | 73.28 | −6.6% | −8.8% | −16.4% | coil-screened only (below 200-SMA — any long is counter-trend) |
| TLN | IPP / nuclear PPA | 307.67 | −15.8% | −14.8% | −31.8% | Live **supply** 343.19, core **4/9** → cut |
| BWXT | Nuclear components | 149.73 | −16.2% | −22.9% | **−38.1%** | No clean zone at either threshold |
| NRG | IPP | 113.61 | −13.5% | −23.7% | **−40.2%** | Demand 132.54 **invalidated** |

NRG is the story in one line: it had an institutional demand zone at 132.54, and on **2026-08-04 it gapped
from 138.47 to a 112.50 low in a single session** — straight through the level, a −15% day. That is not a
pullback, it's a repricing.

### Running tally across both passes

**Fourteen names zone-scanned** — ANET, CEG, GEV, ETN, VRT, PWR, VST, EQIX, EME, FIX (Monday) plus ETR,
TLN, NRG, BWXT (today). Results:

- **Zero live demand zones.** Not one, at either leg-out threshold.
- **Five broken demand zones:** ANET 169.10, CEG 295.28, VRT 349.79, EQIX 1031.47, NRG 132.54 — price
  closed through all five.
- **Four live supply zones**, every one of them either far above spot, below the 6/9 score gate, or with
  its target already reached: VST 167.17 (core 6/9, target already hit), FIX 1979.13 (core 5/9), ETR
  107.34 (core 4/9), TLN 343.19 (core 4/9).
- **Six names with no clean base + leg-out at all:** GEV, ETN, PWR, EME, BWXT, and PEG by inspection.

The direction of the evidence is one-way. In a theme where buyers were defending levels, you would expect
at least one fresh untested demand zone among fourteen names. There are none, and there are five levels
where the defenders were run over. XOM, scanned the same day with the same code, has exactly the fresh
untested zone this theme lacks.

### If you want to stay engaged with data center

**ANET** remains the only structurally intact name in the group (above both moving averages). Its broken
demand at **169.10** is the level to watch — not as an entry, but as a test: if price returns there and
builds a base instead of slicing through, it becomes a real setup.

**ETR** carries a Bollinger-width percentile of **0.02** — a violent squeeze — and is the only DC-power
name still above its 200-day. But its one live zone is *supply*, pointing down. Coiled with a bearish
level is a warning, not a setup.

---

## Method notes

1. **Data through the 2026-08-25 close** — a completed session; XOM's last two bars were re-fetched from
   Massive as full OHLC rather than close-only, so every level traces to retrieved data.
2. **Both thresholds** run on every name: `--leg-mult 1.6` (default) and `1.3` (loosened).
3. **XOM cross-verified on two independent feeds** (Massive/Polygon and FMP) — 165.11, 164.05 and 160.64
   all match to the cent. The data-center names rest on a single feed; FMP's chart endpoint is plan-blocked
   for most of them.
4. **PEG was coil-screened but not zone-scanned** — it sits 8.8% below its 200-day, so a long there is
   counter-trend regardless of what a scan returned.
5. **Lookback:** 60–182 daily bars depending on name.
