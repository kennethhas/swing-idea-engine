# Surge O.E. Scorecards — all four Table-1 names

**Run:** 2026-08-28 · **Data:** daily bars through the 2026-08-27 close · **Feed:** Massive/Polygon
**Framework:** SurgeU Reference Card 2 (v20250123) — 6 enhancers, max 10, 8.5 proximal gate.

> **Scoring history for BAC — read this before trusting any number here.** BAC was scored three
> times in one session: 6.5 (No Trade), then 7.5 (Confirmation), then 6.5 again. **The data never
> changed. Only the Strength denominator did.** Reference Card 2 requires the move-out to be
> "≥2:1" but never says 2:1 *of what*. Measured against zone width BAC is 2.0× (pass); measured
> against ATR it is 1.7× (fail). The second pass silently switched to zone width and was published
> as a "correction" — it was not one, it was a substitution.
>
> **Zone width is the wrong denominator and is now retired.** It is unstable: CSCO's base is 0.26
> ATR wide, so dividing by it returned 14:1 for a 3.6-ATR move (49:1 on a 5-bar window). A measure
> that can print 49:1 is measuring its denominator. **ATR at the formation bar is now pinned** in
> `references/continuation-override.md`. Every score below uses it. **The original 6.5 / No Trade
> for BAC was correct.**

## Read this first: all four zones are BELOW spot

The scorecard grades a *zone*. Every zone here is a discount entry — the thing the continuation
override exists to avoid. Only XOM's is realistically reachable.

| Ticker | Zone (prox/distal) | Spot | Distance below | Continuation trigger (Table 1) |
|---|---|---|---|---|
| XOM | 154.84 / 151.53 | 156.44 | **−1.0%** | 158.71 (+1.5%) |
| BAC | 57.88 / 56.84 | 61.17 | −5.4% | 62.12 (+1.6%) |
| AAPL | 294.38 / 289.19 | 314.58 | −6.4% | 316.29 (+0.5%) |
| CSCO | 92.16 / 91.61 | 112.15 | **−17.8%** | 113.85 (+1.5%) |

CSCO's zone is 17.8% below price. It is a real level; it is not a 2026 trade.

## The scorecards

```
Surge O.E. Scorecard — all four DEMAND zones   (Strength measured vs ATR)
                        XOM     BAC    CSCO    AAPL
  Strength      /2        1       1       2       2    move-out 1.7 / 1.7 / 3.6 / 2.5 ATR
  Time          /1        1       1       1       1
  Freshness     /2        2       2       2       2
  Trend         /2        2       2       1       0
  Curve         /1      0.5     0.5     0.5     0.5
  Profit Zone   /2        0       0       0       0    <- UNKNOWN, scored conservatively
  ──────────────────────────────────────────────────
  TOTAL        /10      6.5     6.5     6.5     5.5
  Band                   Low     Low     Low     Low
  Entry               NO TRADE NO TRADE NO TRADE NO TRADE
```

**All four are NO TRADE. Nothing comes within 2 points of the 8.5 proximal gate.**

XOM and BAC fail the move-out at 1.7 ATR — they walked out of their zones over several
sessions rather than leaving with force. CSCO (3.6) and AAPL (2.5) genuinely departed, and
lose their points on Trend instead.

Flags: **AAPL — against-trend ceiling.** Trend=0 caps it at 8.0, below the floor, so a proximal
entry is impossible there regardless of what else improves.

## Why every Profit Zone is zero

Not four separate failures — one structural fact. **None of the four names has a live opposing
zone.** Every supply zone in all four is invalidated:

| Ticker | Supply zone | Broken on |
|---|---|---|
| BAC | 61.28 | 2026-08-05 |
| CSCO | 117.09 | 2026-08-04 |
| XOM | 148.91 | 2026-07-22 |
| AAPL | 293.08 | 2026-07-02 |

The card requires the target be a real opposing zone proximal and says non-zone levels —
support/resistance, swing highs, analyst targets — do not count. With nothing legal to measure
against, the input is UNKNOWN and the guardrail says score conservatively rather than invent one.

**If you allow the scanner's swing-high targets anyway**, here is what changes:

| Ticker | Swing target | R:R | PZ | Total | Band |
|---|---|---|---|---|---|
| BAC | 65.22 | 7.06 | 2 | **8.5** | Proximal — *by exactly zero margin* |
| CSCO | 130.37 | 69.46 | 2 | **8.5** | Proximal — *by exactly zero margin*, on an UNVERIFIED R:R |
| XOM | 168.64 | 4.17 | 1 | 7.5 | Confirmation |
| AAPL | 344.57 | 9.67 | 2 | 7.5 | Confirmation (trend ceiling holds) |

Nothing clears with daylight. The two that reach the gate land precisely on it, and CSCO's
69.46 R:R is a scanner artifact of a 0.55-wide zone on a $92 stock — flagged UNVERIFIED by the
scanner itself. Qualifying by landing exactly on the floor, via an input the card disallows, is
not a qualification.

## Per-name notes

**XOM — 6.5, No Trade. Still the only reachable zone, and the joint-best structure.**
Fresh untested zone, daily ITF genuinely up (higher highs 159.07 → 161.67 → 168.64, higher low
149.09 → 156.14), base 3 candles. **Its move-out is what fails it: 1.7 ATR.** The 08-10 expansion day looks
decisive on a chart, but relative to XOM's own 4.01 ATR it is an ordinary day's range. Its zone sits 1.0%
under spot while its continuation trigger sits 1.5% over — the two frameworks bracket the price.
**Caveat:** the curve placement is borderline. Zone midpoint 153.19 vs the High-third boundary
153.72 — 0.53 away. Read as High third it becomes the "Long\* ADVANCED" cell (with-trend,
curve-penalized, ceiling 9.0) and the total drops to 7.0.

**BAC — 6.5, No Trade.** Same profile as XOM: fresh, with-trend, and the same 1.7-ATR move-out
failure. Loses on Strength, Curve (mid-range) and Profit Zone. Its zone needed `--leg-mult 1.0` to appear at all — well below
the framework's 1.6 — so the zone itself is soft even though the enhancers grade well.

**CSCO — 6.5, No Trade.** The binding constraint is **Trend**, not Profit Zone. Its daily ITF is
**sideways**, not up: highs 121.61 → 117.28 → 124.71 against lows 111.66 → 110.06 → 109.23 — a
contracting range since the June peak of 130.37. A demand zone in a sideways ITF scores 1, not 2.
Note this does *not* contradict the continuation screen, which gated CSCO on the **100-day**
trend and explicitly flagged it as trading below its 50-day.

**AAPL — 5.5, No Trade, and hard-capped.** Daily ITF reads **down** — lower highs from 344.57 to
316.29 to 320.28. Against-trend caps it at 8.0, so no improvement short of a trend change lets it
qualify. If you read the ITF as sideways instead (defensible — the last two lows, 300.00 and
300.57, are flat rather than lower), it scores 8.5 with the swing target. That is a big swing on
one judgment call; I scored it conservatively. AAPL is also the **only** name with a zone at the
default `--leg-mult 1.6`, which is a point in its favour that the score does not capture.

## Cross-cutting findings

1. **All four zones are FRESH** — not one has been re-entered since formation. Lowest lows since:
   XOM 156.14 (vs 154.84 proximal), BAC 57.94, AAPL 300.00, CSCO 93.14.
2. **All four sit in the MIDDLE third of the weekly curve.** Not one is in the Low third where a
   demand zone wants to be. 52-week ranges: XOM 108.35–176.41, BAC 46.12–65.22,
   CSCO 66.13–130.37, AAPL 225.95–344.57.
3. **Zone quality degrades as you loosen.** AAPL has a zone at 1.6 (the default); XOM and CSCO
   need 1.3; BAC needs 1.0. The scan threshold required is itself a quality signal.
4. **Nothing has live supply overhead.** Four for four. Read constructively that is bullish — no
   institutional selling parked above — but mechanically it makes the card's Profit Zone
   unmeasurable, which is why the whole slate lands on NO TRADE.

## Method notes

- Strength: move-out = (highest high within 3 bars of formation − proximal) ÷ **ATR at the
  formation bar**, ≥2.0; breakout = post-formation high exceeds the prior 40-bar swing-pivot
  high. **The card shows 2:1 visually without naming the denominator** — ATR is a chosen
  denominator, pinned in `references/continuation-override.md` after zone width proved unstable.
  Raw ratios: CSCO 3.6, AAPL 2.5, XOM 1.7, BAC 1.7. Overrule the category if you read the charts
  differently; the ratios are there for that.
- Trend from a 3-pivot HH/HL vs LH/LL sequence over the last 60 daily bars.
- Curve from the 52-week daily high/low split into thirds, zone located by midpoint.
- Freshness by depth of deepest re-entry as % of proximal→distal width, per the card — not touch
  count.
- Single feed. Levels expire at the next open. Educational analysis, not financial advice.
