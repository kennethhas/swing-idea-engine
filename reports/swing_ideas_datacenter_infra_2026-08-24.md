# Data Center / AI Infrastructure — Zone-Gated Swing Screen

**Run date:** 2026-08-24 · **Data as-of:** 2026-08-21 close (today's partial bar excluded from all scans)
**Regime:** SELECTIVE · **Not financial advice.** Levels expire at the next session's open.

---

## Verdict: no qualifying setup. Zero of ten.

I scanned the full data-center stack — power generation, electrical & thermal, networking silicon,
engineering contractors, and the REITs — at both the default leg-out threshold and the loosened one.
**Not a single live demand zone exists anywhere in this theme.**

That is not the scanner failing to find something. It is the scanner finding something specific, and it
took the same form in name after name: **the demand zones didn't survive — price closed straight through
them.**

| Ticker | Role in the stack | Demand zone that broke | Broken on |
|---|---|---|---|
| ANET | Networking silicon | 169.10 / 162.59 | invalidated |
| CEG | Nuclear power gen | 295.28 / 276.84 | invalidated |
| VRT | Power & cooling hardware | 349.79 / 339.71 | invalidated |
| EQIX | Data-center REIT | 1031.47 / 1024.04 | invalidated |

Four of the theme's anchor names had an institutional demand level, and price cut through all four. In
GEV, ETN, PWR and EME the scanner found **no clean base + leg-out at all**, at either threshold — the
signature of a name in open-ended decline rather than one resting.

Contrast this with what turned up in Energy and Aerospace earlier today: XOM and HWM both had **fresh,
untested** demand zones that price had never returned to. Same framework, same session, opposite result.
Here the buyers who defended those levels have already been run over. Mechanically, that is distribution,
not accumulation.

---

## The two live zones — both supply, both unusable

| Ticker | Zone | Type | Core | Why it's cut |
|---|---|---|---|---|
| VST | 167.17 / 169.60 | supply (short) | 6/9 | Entry sits **22.7% above** spot 136.21 — nowhere near tradeable. Worse, its target of 134.75 has *already been reached*; the move is spent. |
| FIX | 1979.13 / 2073.99 | supply (short) | **5/9** | Fails the ≥6 score gate, and entry is 19.5% above spot 1655.61. |

Both are shorts pointing down, in a theme already down hard — late, not early. Neither is a trade.

---

## The damage, quantified

Every name in the cohort is well off its 52-week high, and only one is above its 50-day moving average.

| Ticker | Close | ATR %ile | BB %ile | vs 50-SMA | vs 200-SMA | % from 52w high |
|---|---|---|---|---|---|---|
| ANET | 188.15 | 0.40 | 0.60 | **+5.7%** | **+26.1%** | −12.4% |
| ETN | 408.67 | 0.13 | 0.93 | −1.9% | +7.7% | −14.5% |
| EME | 764.90 | 0.17 | 0.89 | −4.0% | +1.4% | −19.6% |
| GEV | 942.10 | 0.21 | 0.43 | −9.0% | +8.3% | −21.2% |
| PWR | 616.78 | 0.78 | 0.76 | −8.0% | +6.3% | −21.8% |
| FIX | 1609.69 | 0.42 | 0.45 | −9.5% | +10.0% | −22.4% |
| VRT | 254.97 | 0.24 | 0.67 | −13.0% | +0.6% | −32.9% |
| CEG | 273.43 | 0.10 | **0.01** | +3.7% | **−8.7%** | −33.7% |
| VST | 135.66 | **0.00** | 0.21 | −11.4% | **−15.0%** | −38.3% |

*(EQIX scanned but not coil-screened — both its zones invalidated regardless.)*

**ANET is the only name in the group still structurally intact** — above both moving averages, and the
shallowest drawdown in the cohort. Everything else has lost its 50-day; CEG and VST have lost their
200-day outright.

---

## If you want to stay engaged with the theme

Nothing here is a trade today. Two names are worth a watchlist slot, for opposite reasons:

**ANET — the only intact chart.** Its broken demand at **169.10** is the level that matters: 10.4% below
spot 188.15. If price returns there and *rebuilds* a base rather than slicing through, that becomes a real
setup. Right now it is a broken level, and broken levels are not entries.

**CEG — the tightest coil in the entire session.** Bollinger-width percentile **0.01**, meaning its bands
are narrower than 99% of the past six months. Range compression 0.61, volume dry-up 0.80. Something is
loading. But readiness ranks the probability of *a move*, not its direction, and CEG is 8.7% below its
200-day — so the coil is as likely to release downward. Direction has to come from a level, and CEG
doesn't have a live one. Watch, don't anticipate.

---

## Method notes

1. **Ten names scanned:** ANET, CEG, GEV, ETN, VRT, PWR, VST, EQIX (data-center core) plus EME, FIX
   (broader infrastructure / engineering & construction).
2. **Both thresholds tried** — `--leg-mult 1.6` (default) and `1.3` (loosened). The loosening is what
   surfaced XOM and HWM earlier today; here it surfaced nothing usable, which strengthens the read rather
   than weakening it.
3. **Today's in-progress bar was excluded** from every scan; all zones derive from completed sessions
   through 2026-08-21. Coil-screen closes are stamped 2026-08-24 (live).
4. **Lookback:** 95–120 daily bars per name (roughly 5–6 months).
5. **Single feed.** These levels come from Massive/Polygon aggregates only; FMP's chart endpoint is
   plan-blocked for most of these symbols, so no cross-feed confirmation was possible. Verify on
   TradingView before acting on any of them.
6. **No earnings checks were run** — moot, since nothing qualified.
