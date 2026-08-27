# Odds Enhancers Reference (Seiden / OTA)

The scoring system that separates a tradable zone from a level you should skip. The goal of the framework is to take only the highest-probability, lowest-risk zones — most zones should be *rejected*.

Score the five **core** enhancers (max 9) for every zone, then note the two **extended** ones qualitatively. Always show the breakdown so the arithmetic is transparent and the user can override any single score.

---

## Core enhancers (max 9)

### 1. Strength of the Move — max 2
*How did price leave the level?* The faster and larger the leg-out, the more out of balance supply/demand was — that's the whole signal.
- **2** — explosive departure: large momentum candles, price travels far fast, little overlap.
- **1** — clear but moderate move away.
- **0** — slow, grinding, overlapping exit (weak imbalance).

From data: compare the leg-out candles' range/body to the base candles and to recent average range (ATR). Big multiple → 2.

### 2. Reward / Risk (Profit Margin) — max 2
Two questions: (a) how far did price travel away from the level before returning (initial profit margin), and (b) how far is the **nearest opposing zone** that you'd target?
- **2** — large initial move off the level **and** ≥3:1 reward:risk to the opposing zone.
- **1** — decent margin, roughly 2:1.
- **0** — opposing supply/demand sits close; poor R:R. *Skip these even if everything else is good.*

Rule of thumb (Seiden): a demand level only "counts" if the initial rally was at least ~3x the zone height (the risk). Same logic inverted for supply.

### 3. Big Picture — max 2
Where does the zone sit relative to the higher-timeframe trend and structure? You want to trade *with* the larger trend and *into* larger support/demand or resistance/supply.
- **2** — zone aligns with the higher-timeframe trend and sits at meaningful higher-timeframe structure (e.g., buying demand in an uptrend near big-picture support).
- **1** — neutral / mixed context.
- **0** — fighting the higher-timeframe trend (e.g., shorting a supply zone just above strong big-picture demand). Downgrade hard.

Always glance at a higher timeframe before finalizing this score; it's the enhancer most often skipped and most often decisive.

### 4. Retracements / Tests (Freshness) — max 2
How many times has price returned to the zone since it formed? Each return consumes resting orders ("the mass"), so fresh zones are strongest.
- **2** — first return (untested, fresh).
- **1** — second return.
- **0** — third return or more.
Mental model: every swing into the level is like another chop at a tree — the more swings, the more likely it finally breaks through.

### 5. Time at Level — max 1
How many candles did price spend basing? Less time = more imbalance. Tightly coupled to Strength.
- **1** — very few candles in the base (tight, brief pause).
- **0** — many candles / extended consolidation.
*Do not anchor to an absolute candle count* — it changes with timeframe. Compare this base's duration to other bases on the same chart.

---

## Extended enhancers (qualitative — note, don't force a number)

### Arrival
*How is price approaching the zone right now?* A strong, fast, momentum-driven approach into the level tends to produce a cleaner reaction than a slow, grinding drift into it (which often just leaks through). Note "strong arrival" / "weak arrival / drifting in" as a flag on the trade plan, especially for set-and-forget limit entries.

### Curve
*Where does the zone sit within the larger price range/channel?* Buy demand zones low in the curve (oversold side), sell supply zones high in the curve (overbought side). A demand zone sitting near the top of an extended range is lower-odds even if its other scores are high. Note the curve location qualitatively.

---

## Putting it together

- Sum the core enhancers → `score/9`.
- Practical filter: zones scoring **roughly 7-9** are A-setups; **5-6** are marginal (need strong extended context); **below 5** are normally skipped.
- A failing **Reward/Risk (enhancer 2)** or a **0 on Big Picture** can veto an otherwise high score — call this out explicitly rather than letting the total mask it.
- Report the per-enhancer breakdown every time. If you adjusted a score from the scanner's programmatic guess (common for Big Picture, Arrival, Curve), say so and why.

## Important honesty note

These scores are a *disciplined heuristic*, not a validated predictive model. They encode a coherent logic (imbalance leaves a footprint; fresh footprints react; trade with the trend and with good R:R), and that logic is sound risk management. But high scores do not guarantee outcomes, the framework has no peer-reviewed edge, and zone selection remains partly subjective. Present results as "higher-probability, well-defined-risk setups," never as predictions.
