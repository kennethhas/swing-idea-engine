# Decision Matrix + ATH Rule

> ⚠️ **DRAFT — RECONSTRUCTED, NOT CONFIRMED.** Kenneth has not yet supplied his
> OTA-card Decision Matrix or ATH rule text. The matrix below is reconstructed
> from the Seiden/OTA framework and how his past verdicts (ORCL, NFLX, TQQQ,
> CVX) were actually decided. When using it, state the cell applied and flag
> that the matrix is a draft, so drift from his card gets caught and corrected.
> Once Kenneth confirms or replaces this, delete this warning block.

## Matrix — Curve location × Daily ITF trend → action

Curve location = where price sits between the nearest live weekly demand
(bottom of curve) and nearest live weekly supply (top of curve).

| | ITF Uptrend (HH/HL, > SMA20/50) | ITF Sideways | ITF Downtrend (LH/LL, < SMA20/50) |
|---|---|---|---|
| **Low on curve** (at/near live fresh demand) | **BUY** at proximal — best long cell | **BUY** at proximal with confirmation | **BUY only on zone hold** — counter-ITF, HTF-reversal trade; demand LOW-conviction if pass-2 |
| **Mid curve** | WATCH — no proximal entry without chasing | **NO TRADE** — no edge either side | WATCH — wait for arrival at demand |
| **High on curve** (at/near live fresh supply) | **SHORT** at proximal with confirmation (counter-ITF) — executability flag | **SHORT** at proximal — executability flag | **SHORT** at proximal — best short cell — executability flag |

Degenerate cases:
- **Curve undefined (zero live supply):** branch on ITF trend. In a
  **downtrend/range** the long has no target → capped at WATCH. In a **confirmed
  uptrend this is blue-sky continuation** — do NOT auto-cap: route to the
  continuation trigger (SKILL Step 5) with a projected target, and demote any
  demand zone >~7% below price to a labeled backup limit. Short side inapplicable
  (shorting blue sky fights the trend).
- **Zero live demand:** short side has no target → short capped at WATCH.
- Every cell is still subject to ALL hard gates (earnings, freshness, 3:1,
  6/9 score, target existence). The matrix chooses direction; gates decide
  eligibility.

## ATH rule

> ⚠️ **DRAFT.** At/near ATH there is no overhead supply by definition. This does
> NOT mean "no long" — it means the target is a **projection** (measured move /
> ATR extension / prior high), not a zone, and the entry is neither the extended
> ATH print (that is the chase) NOR a deep demand zone (a fill a running trend
> won't give). The entry is the **continuation trigger** (SKILL Step 5): the first
> higher-low base that holds, or a reclaim-close above the last lower-high after a
> pullback. Chasing the vertical print = no; a with-trend pullback-continuation
> entry with a projected target = yes. Shorting blue sky = fighting the trend, no.
