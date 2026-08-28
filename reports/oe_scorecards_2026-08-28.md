# Surge O.E. Scorecards — all four Table-1 names

**Run:** 2026-08-28 · **Data:** daily bars through the 2026-08-27 close · **Feed:** Massive/Polygon
**Framework:** SurgeU Reference Card 2 (v20250123) — 6 enhancers, max 10, 8.5 proximal gate.

> **Correction to the BAC score given earlier this session.** I scored BAC's Strength 1/2 using
> `zone_scanner.py`'s leg-vs-ATR reading. That is the scanner's operational proxy, and
> `references/thresholds.md` says explicitly it is *not* the card's definition. Measured the
> card's way — move-out leg and break of prior structure, each ≥2:1 — BAC is **2/2**
> (move-out 2.8×, structure break 4.9×). **BAC moves 6.5 → 7.5: No Trade → Confirmation entry.**
> The same correction applies to XOM and AAPL, where the scanner also read Strength low.

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
Surge O.E. Scorecard — all four DEMAND zones
                        XOM     BAC    CSCO    AAPL
  Strength      /2        2       2       2       2
  Time          /1        1       1       1       1
  Freshness     /2        2       2       2       2
  Trend         /2        2       2       1       0
  Curve         /1      0.5     0.5     0.5     0.5
  Profit Zone   /2        0       0       0       0     <- UNKNOWN, scored conservatively
  ──────────────────────────────────────────────────
  TOTAL        /10      7.5     7.5     6.5     5.5
  Band                Medium  Medium     Low     Low
  Entry                Confirm Confirm  NO TRADE NO TRADE
```

**Nothing reaches 8.5. No proximal limit entry on any of the four.**

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
| BAC | 65.22 | 7.06 | 2 | **9.5** | Proximal |
| XOM | 168.64 | 4.17 | 1 | **8.5** | Proximal — *by exactly zero margin* |
| CSCO | 130.37 | 69.46 | 2 | **8.5** | Proximal — *by exactly zero margin*, on an UNVERIFIED R:R |
| AAPL | 344.57 | 9.67 | 2 | 7.5 | Confirmation (trend ceiling holds) |

Only BAC clears with any daylight. Two land precisely on the gate, and CSCO's 69.46 R:R is a
scanner artifact of a 0.55-wide zone on a $92 stock — the scanner itself flags it UNVERIFIED.

## Per-name notes

**XOM — 7.5, Confirmation. The best of the four, and the only reachable one.**
Fresh untested zone, daily ITF genuinely up (higher highs 159.07 → 161.67 → 168.64, higher low
149.09 → 156.14), base 3 candles, move-out 2.1× on the 08-10 expansion day. Its zone sits 1.0%
under spot while its continuation trigger sits 1.5% over — the two frameworks bracket the price.
**Caveat:** the curve placement is borderline. Zone midpoint 153.19 vs the High-third boundary
153.72 — 0.53 away. Read as High third it becomes the "Long\* ADVANCED" cell (with-trend,
curve-penalized, ceiling 9.0) and the total drops to 7.0.

**BAC — 7.5, Confirmation.** Same profile as XOM: fresh, with-trend, strong departure. Loses on
Curve (mid-range) and Profit Zone. Its zone needed `--leg-mult 1.0` to appear at all — well below
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
   unmeasurable, which is why the whole slate tops out at Confirmation.

## Method notes

- Strength measured as: move-out = (highest high within 5 bars of formation − proximal) ÷ zone
  width, ≥2:1; breakout = post-formation high exceeds the prior 40-bar swing high. **The card
  shows 2:1 visually without naming the denominator**; zone width is my choice, stated so it can
  be overridden. The scanner's ATR proxy disagrees on BAC (0), XOM (1) and AAPL (1).
- Trend from a 3-pivot HH/HL vs LH/LL sequence over the last 60 daily bars.
- Curve from the 52-week daily high/low split into thirds, zone located by midpoint.
- Freshness by depth of deepest re-entry as % of proximal→distal width, per the card — not touch
  count.
- Single feed. Levels expire at the next open. Educational analysis, not financial advice.
