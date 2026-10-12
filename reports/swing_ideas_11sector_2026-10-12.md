# Swing Idea Engine — 11-Sector Screen

**Run:** 2026-10-12 (scheduled routine) · **Price data as-of:** 2026-10-09 close (last completed session)
**Variant:** Balanced · **Universe screened:** 27 names, 11 sectors · **Survived all gates:** 4

> Educational analysis under a defined framework, **not financial advice**. Entry/stop/target are
> levels where a setup becomes valid — not predictions. Position sizing is the trader's call.

---

## Data provenance — read this first

**The repository contains no stored market data.** `kennethhas/swing-idea-engine` holds only the
skill definition and four scripts (`regime_gate.py`, `squeeze_scan.py`, `zone_scanner.py`,
`data_sources.py`), all of which fetch live at run time. There is no cached price file, indicator
snapshot or sector table to read, so "query the repo for the latest market data" has no stale-data
failure mode — it has **no data at all** by design.

Worse, **the scripts' own feeds are unreachable from this environment.** The egress policy denies
CONNECT to `query1.finance.yahoo.com` (primary), `quote.cnbc.com` (cross-feed) and `stooq.com`
(legacy fallback), plus every other market-data host probed. Verified, not assumed.

Substituted live feeds, both reached through MCP:

| Feed | Role | Coverage here |
|---|---|---|
| Massive (Polygon-lineage) `/v2/aggs` | primary OHLCV, all 27 names | full; rate-limited to ~5 calls/window |
| FMP `historical-price-eod-full` | cross-feed check | **2 of 27 symbols** (AAPL, XOM) — plan tier denies the rest |
| FMP `earnings-calendar` | earnings-buffer gate | partial/curated list (~45 names over 3 weeks) |

Consequences, stated plainly:
- The bundled scripts ran **unmodified** on locally staged CSVs. `regime_gate.py` has no `--csv`
  option, so its `posture()`/`verdict()` functions were called through a read-only shim that
  substitutes the CSV loader for the Yahoo fetch. No repo code was edited.
- Step 3's cross-feed check could only run on **AAPL and XOM** — both **AGREE** (0.00% on close,
  high and low; volume agrees to <0.01%). **V and PANW are ONE-SOURCE** and tagged as such.
- Where the two feeds do overlap they agree to 4–6 significant figures on price *and* volume, which
  suggests a **shared upstream** rather than two genuinely independent providers. Treat the AGREE
  verdicts as weaker corroboration than the skill's design assumes.
- Massive reports sub-share volume precision (e.g. `8,086,540.877`) from 2026-02-23 onward for every
  symbol. Initially flagged as possible modeled data; **checked and cleared** — FMP carries the same
  magnitudes rounded to whole shares, so it is an upstream precision change, not synthetic volume.

**Recommended refresh:** allow `query1.finance.yahoo.com` and `quote.cnbc.com` through the egress
policy so the scripts run as designed, or upgrade the FMP plan so a real second feed covers the whole
universe. Until one of those happens, every level below rests on a single provider.

---

## STEP 0 — Regime gate (`regime_gate.py`, unmodified logic)

```
SPY @ 778.57 (2026-10-09): CONSTRUCTIVE — longs favored   vs50=+1.4%  vs200=+7.7%   loc-in-20d-range=90%
QQQ @ 751.27 (2026-10-09): CONSTRUCTIVE — longs favored   vs50=+3.7%  vs200=+11.8%  loc-in-20d-range=82%

VERDICT: GREENLIGHT — broad tape constructive; demand-zone longs are with-regime
```

Both indices sit above a rising 50- over 200-SMA and in the top decile of their 20-day range. Demand-zone
longs are with-regime, and **limit-in entries are permitted** by the skill under GREENLIGHT.

The same reading explains the thinness of what follows: with indices pinned near highs, almost every
demand zone has been left far below price, and the nearest overhead target is frequently *the current
price itself*. That is a structural feature of this tape, not a screening failure.

---

## A. Ranked by conviction (coil + gated zone + regime + arrival)

| # | Ticker | Sector | Entry (proximal) | Stop | T1 | T2 | R:R (real) | Odds | Coil | Tier | Trigger | Feeds |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **XOM** | Energy | 154.84 | 151.20 | 170.29 | NA | **4.24:1** | 8/9 | 83.8 COILED | A | Limit-in OK (GREENLIGHT) or reclaim close >154.84 | AGREE |
| 2 | **AAPL** | Technology | 294.38 | 288.68 | 345.34 | NA | **8.94:1** | 8/9 | 76.3 COILED | B | Confirmation — reclaim close >294.38 | AGREE |
| 3 | **V** | Financial | 360.66 | 356.36 | 386.84 | NA | **6.09:1** | 8/9 | 51.4 neutral | C | Confirmation only — weekly conflict below | ONE-SOURCE |
| 4 | **PANW** | Technology | 339.31 | 326.87 | 432.32 | NA | **7.48:1** | 7/9 | 68.0 building | C | Watch — entry 19% away | ONE-SOURCE |

All four are **demand (long) setups, with-regime**. No short setup survived.

R:R is recomputed to the **actual stop**, never the distal line. The scanner's headline figure ran
**9.0–9.2% high on every single name** — exactly the inflation the skill's reference warns about
(e.g. XOM headline 4.67 vs tradeable 4.24).

**T2 is `NA` for all four.** Each sits in open space with no second opposing zone overhead. Honest `NA`,
not a missing lookup.

---

## B. By sector (the scannable list)

### ⚡ Energy — 1 setup
- **XOM — LONG @ 154.84** · stop 151.20 · T1 170.29 · R:R 4.24:1 · 8/9 · **coil 83.8 (COILED)**
  - *Why:* Drop-Base-Rally demand, untested, 8.3% below spot (168.94). Tightest coil in the whole
    universe — ATR% in the **0.8th percentile** of its 6-month range, BB width 9.5th percentile,
    volume dried to 0.81× — inside a clean uptrend. Weekly shows no supply overhead; the zone sits in
    open space.
  - *Earnings:* 2026-10-30 — 13 trading days out, clears the 5-day buffer, but **inside the likely
    holding window** if the entry fills late. Size for the gap or plan to be out before it.
  - *Why this might be wrong:* XOM is coiling 8% **above** the zone near its high, so the likeliest
    resolution is an upside break that never fills the limit — and T1 (170.29) is only +0.8% over
    spot, so the paid reward is a dip-and-recover round trip, not fresh upside.
- COP (coil 70.8), SLB (53.3) — cut, see footer.

### 📡 Communication Services — **no qualifying setup**
- GOOGL is the second-tightest coil in the screen (**79.7 COILED**, BB width 2.4th percentile, uptrend)
  and META reads 75.9 — but **neither presents a live zone**. Every detected zone on both is
  invalidated: price has closed through all of them. Coil says "a move is loading"; the zone scan says
  "no defensible level to trade it from." That disagreement is signal — these are the names to re-scan
  first after any pullback builds a fresh base. Both report 2026-10-28.
- DIS (67.2) — no live zone.

### 🛍️ Consumer Cyclical — **no qualifying setup**
- NKE carries a 7/9 supply zone at 45.52 with 7.32:1, but it is **31% above** spot (34.71) — a
  level, not a trade.
- HD 4/9, LOW 5/9 — both below the 6/9 floor.

### 🥫 Consumer Defensive — **no qualifying setup**
- KO's 8/9 demand at 68.01 is **22.8% below** spot and recomputes to **28.2:1** — a stale-target
  artifact, flagged UNVERIFIED, not an edge.
- PEP supply at 154.62 is 22.7% above spot. PG — no live zone.

### 💻 Technology — 2 setups
- **AAPL — LONG @ 294.38** · stop 288.68 · T1 345.34 · R:R 8.94:1 · 8/9 · **coil 76.3 (COILED)**
  - *Why:* Rally-Base-Rally demand, fresh (untested), with the weekly uptrend and no weekly supply
    overhead — the prior weekly supply at 333.02 is already invalidated beneath spot (336.64).
    ATR% 12.7th percentile, BB width **0.8th percentile** — the tightest Bollinger pinch in the screen.
  - *Only name besides XOM corroborated by two feeds* (FMP + Massive AGREE to the cent).
  - *Earnings:* 2026-11-02. Clears the 5-day buffer; **will almost certainly fall inside the hold**
    given the entry is 12.6% below spot.
  - *Why this might be wrong:* a 12.6% drawdown in AAPL implies a tape that no longer looks like
    today's GREENLIGHT, so the setup and its regime assumption probably cannot both be true at fill.
- **PANW — LONG @ 339.31** (watch) · stop 326.87 · T1 432.32 · R:R 7.48:1 · 7/9 · coil 68.0
  - *Why:* Drop-Base-Rally demand with the weekly uptrend; a second, wider zone at 338.49 (5.00:1)
    overlaps it, which thickens the shelf. Entry is **19% below** spot (418.78) — listed as a resting
    level, not an actionable week-ahead entry. ONE-SOURCE.
- AMAT (coil 60.8) — nearest zone 62% below spot, R:R 179:1. Cut, UNVERIFIED.

### 🏥 Healthcare — **no qualifying setup**
- MRK coils at 68.2 but its 8/9 demand sits **45.9% below** spot at 78.76 and recomputes to 66.8:1 —
  UNVERIFIED stale target. MDT (35.9) — coil already released, no live zone.

### 🏢 Real Estate — **no qualifying setup**
- SPG (61.0) and PLD (42.4) — no live zone at either detection threshold.

### ⛏️ Basic Materials — **no qualifying setup**
- **FCX is the standout disagreement:** coil **82.1 (COILED)** in a clean uptrend — second-tightest in
  the screen — and **zero live zones**. Highest-readiness name with nothing to trade it from. Top of
  the re-scan list.
- NUE (60.3) — no live zone.

### 🏦 Financial — 1 setup (1 cut on earnings)
- **V — LONG @ 360.66** · stop 356.36 · T1 386.84 · R:R 6.09:1 · 8/9 · coil 51.4 · **Tier C**
  - *Why C despite 8/9:* three independent problems. (1) **T1 386.84 is essentially spot (385.45)** —
    the reward is a round trip back to today's price. (2) **Weekly conflict:** live weekly demand sits
    at 381.35, *above* the daily entry, so 360.66 only fills after that weekly shelf fails — the entry
    is conditional on weekly weakness, which argues against the long. (3) Coil 51.4 is neutral: no
    energy is building here. ONE-SOURCE.
  - *Earnings:* 2026-10-27.
  - *Why this might be wrong:* the entry requires a weekly demand failure, and a tape that breaks
    weekly demand is not one that then obligingly rallies back to spot.
- **JPM — CUT.** The zone itself passed every gate (DBD supply @ 347.89, 7/9, 3.14:1, +4.5% above spot
  — the single closest-to-price qualifying zone in the screen). It is cut on the **earnings buffer:
  JPM reports 2026-10-13, tomorrow.** Worth re-scanning Wednesday once the print is out.

### 💡 Utilities — **no qualifying setup**
- **NEE was the closest miss in the entire screen.** DBD supply @ 79.26, only **+2.4% above** spot
  (77.38), 6/9 — genuinely actionable distance. It fails on R:R: the scanner's headline 2.79 measures
  to the distal line, and at the **actual stop (81.17) it is 2.54:1**, under the 3:1 gate. Cut, not
  downgraded. This is precisely the inflation the R:R-to-actual-stop rule exists to catch.
- VST (coil 12.9, most expanded in the screen) — 4/9.

### 🏭 Industrials — **no qualifying setup**
- ETN coils at 71.3 (uptrend) with no live zone. CAT's two 6/9 demand zones are 34–37% below spot with
  26:1 and 46:1 R:R — UNVERIFIED stale targets.

---

## C. Pre-momentum (coil) screen — full universe

Ranked by readiness. **COILED ≥70 · TIGHTENING 55–69 · NEUTRAL 40–54 · EXPANDED <40.**

| Ticker | Sector | Close | Readiness | Zone outcome |
|---|---|---|---|---|
| XOM | Energy | 168.94 | **83.8** | ✅ setup #1 |
| FCX | Basic Materials | 73.69 | **82.1** | ❌ no live zone |
| GOOGL | Communication | 351.66 | **79.7** | ❌ no live zone |
| AAPL | Technology | 336.64 | **76.3** | ✅ setup #2 |
| META | Communication | 718.67 | **75.9** | ❌ no live zone |
| ETN | Industrials | 429.65 | **71.3** | ❌ no live zone |
| COP | Energy | 134.10 | **70.8** | ❌ no live zone |
| MRK | Healthcare | 145.60 | 68.2 | ❌ zone 46% away |
| PANW | Technology | 418.78 | 68.0 | ⚠️ setup #4 (19% away) |
| DIS | Communication | 108.05 | 67.2 | ❌ no live zone |
| KO | Consumer Defensive | 88.05 | 67.1 | ❌ R:R UNVERIFIED |
| SPG | Real Estate | 199.42 | 61.0 | ❌ no live zone |
| AMAT | Technology | 507.03 | 60.8 | ❌ zone 62% away |
| NUE | Basic Materials | 250.33 | 60.3 | ❌ no live zone |
| NEE | Utilities | 77.38 | 59.5 | ❌ R:R 2.54:1 |
| LOW | Consumer Cyclical | 186.00 | 58.0 | ❌ 5/9 |
| JPM | Financial | 332.99 | 54.4 | ❌ earnings 10-13 |
| SLB | Energy | 48.95 | 53.3 | ❌ 5/9 |
| HD | Consumer Cyclical | 290.74 | 51.6 | ❌ 4/9 |
| V | Financial | 385.45 | 51.4 | ⚠️ setup #3 |
| PG | Consumer Defensive | 151.23 | 50.2 | ❌ no live zone |
| CAT | Industrials | 800.47 | 48.3 | ❌ R:R UNVERIFIED |
| PEP | Consumer Defensive | 125.97 | 44.2 | ❌ zone 23% away |
| PLD | Real Estate | 129.49 | 42.4 | ❌ no live zone |
| MDT | Healthcare | 88.48 | 35.9 | ❌ coil released |
| NKE | Consumer Cyclical | 34.71 | 29.8 | ❌ zone 31% away |
| VST | Utilities | 161.48 | 12.9 | ❌ 4/9 |

**Seven names read COILED (≥70); only two of them produced a tradeable zone.** The engine is finding
energy without finding levels — the signature of a tape that has trended far enough to invalidate its
own structure.

---

## Footer (mandatory)

**23 of 27 names cut.** Each with its reason:

| Reason | Count | Names |
|---|---|---|
| No live zone (all detected zones invalidated — price closed through) | 11 | COP, GOOGL, META, DIS, PG, MDT, PLD, SPG, FCX, NUE, ETN |
| Zone not at actionable distance (>20% from spot) | 5 | KO (-22.8%), PEP (+22.7%), NKE (+31.1%), CAT (-34.2%), MRK (-45.9%) |
| Core odds score below 6/9 | 4 | HD (4), LOW (5), SLB (5), VST (4) |
| R:R below 3:1 at the actual stop | 1 | NEE (2.54:1 real vs 2.79 headline) |
| Earnings inside the 5-day buffer | 1 | JPM (reports 2026-10-13) |
| Zone 60%+ below spot with UNVERIFIED R:R | 1 | AMAT (-62.4%, 179:1) |

**Disclosed deviations from the default run:**
1. **Loosened zone detection.** At the default `--leg-mult 1.6`, only AAPL and V produced a qualifying
   live zone across all 27 names; the scanner's own message on the rest was *"No clean base+leg-out
   zones detected… Loosen --leg-mult."* A second pass at **`--leg-mult 1.3`** surfaced XOM, PANW, JPM,
   NEE, KO, NKE, PEP, MRK, CAT and AMAT. XOM and PANW enter the table from that looser pass and carry
   this caveat: their leg-outs are weaker than a default run demands.
2. **Actionable-distance screen.** The skill's gates do not cut on distance-to-zone; its "Arrival"
   enhancer is explicitly discretionary. I applied an explicit threshold — **≤10% actionable,
   10–20% watch, >20% cut** — because a zone 46% below spot is not a swing-trade entry whatever it
   scores. This is my judgment call, flagged as such, and it is what removed KO, PEP, NKE, CAT and MRK
   rather than any mechanical gate.
3. **Visual confirmation not performed.** Big Picture, Arrival and Curve are first-pass heuristics here.
   Big Picture was adjusted by reading each name's weekly zone map (which is how V was downgraded to C).
   Curve is mid-range and undefined for most names — stated rather than scored.

**Overall confidence: 0.45.** The mechanics are sound and reproducible — regime, coil and R:R all
recomputed and audited, and the two cross-checkable names agree exactly. Confidence is held down by
three things, in order: the single-provider feed for V and PANW, the loosened detection threshold
behind two of the four setups, and the fact that **every surviving T1 is at or barely above spot**,
which means none of these four offers genuinely fresh upside — they offer dip-and-recover round trips.

**A 4-name table across 11 sectors is the honest output, not a shortfall.** Eight sectors have no
qualifying setup today. The engine was not padded to fill them.

**Standing reminders:** every level expires at the next session's open — re-verify before order entry.
Levels derive from one unofficial feed (two for AAPL and XOM, probably sharing an upstream). Cross-check
on TradingView before risking capital. The earnings-buffer gate was checked against a **partial**
calendar feed, so absence from it is weak evidence — confirm each report date independently. Not
financial advice.

**Artifacts:** per-name Excel workbooks (one row per zone, every enhancer column) in
`reports/workbooks/zones_{XOM,AAPL,V,PANW}_2026-10-09.xlsx`.

**Next run should:** re-scan JPM after the 10-13 print (closest-to-price qualifying zone in the screen);
re-scan FCX, GOOGL, META and ETN for a fresh base (high coil, no level); and re-check whether Yahoo/CNBC
egress or a higher FMP tier has restored a real second feed.
