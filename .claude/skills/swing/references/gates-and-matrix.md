# Locked gates, verdict logic, and the direction matrix

Read this at the start of every `/swing` run. `scripts/gates.py` implements the
table below; if the two ever disagree, the script is the source of truth and this
file is stale — fix the file.

## Horizon profile (inherited verbatim from deep-dive-swing)

| Layer | TF | Job | Lookback |
|---|---|---|---|
| HTF | **Weekly** | curve location / SMA200 context **only** | 5 years |
| ITF | **Daily** | fixes the trend (HH/HL vs LH/LL, SMA20/50) | 2 years |
| LTF | **240min** | **zones AND entry** | ~6 months of 60m resampled to true 4H |

Zones and entries come from the 240min LTF, **never** the weekly. The weekly only
locates price in the curve; the daily only fixes the trend. Deviate only if the
user names different timeframes, and restate the profile in the output header.

## Hard gates

| Gate | Rule | Effect on failure |
|---|---|---|
| Bars | ≥ 60 LTF (240min) bars | INELIGIBLE, stop the scan |
| Side of price | demand below price / supply above | INELIGIBLE |
| Price-inside-zone | price must be outside the zone | **WATCH cap** (not ineligible) |
| Target | a live opposing zone must exist; long → nearest live supply above, short → nearest live demand below. May come from 240min → daily → weekly; **state which TF** | INELIGIBLE regardless of R:R |
| R:R | **≥ 3:1, both directions**, measured to the *actual stop* | INELIGIBLE |
| Artifact R:R | > ~15:1 | flagged UNVERIFIED, not sold as a good trade |
| Freshness | tested ≤ 1× | INELIGIBLE |
| Odds score | ≥ 6/9 | INELIGIBLE |
| Earnings | > 5 trading days from entry. ETFs use top-weight constituents. **Applies to shorts equally — gap risk is uncapped.** An unverified date is treated as blocking | INELIGIBLE |
| Pass-2 zone | found only at loosened `--leg-mult 1.3` | **WATCH cap**, LOW-CONVICTION |
| Short executability | shorting enabled AND ticker borrowable | flag until confirmed |

### R:R is measured to the actual stop

```
risk   = |proximal − stop|          # stop sits just beyond the distal
reward = |target − proximal|
R:R    = reward / risk
```

A scanner's headline R:R often measures to the *distal* line, which inflates it.
Gate on the number above. If the two disagree, report both and say so.

### Verdict logic

```
any hard-fail                      -> INELIGIBLE
price inside zone, or pass-2 only  -> WATCH   (can never be TRADE)
otherwise                          -> TRADE
```

### Breakeven anchor

At the 3:1 floor, breakeven is a **25% win rate** — right one time in four and you
are flat. Judge the system against that, not against a feeling.

| R:R | breakeven win rate |
|---|---|
| 3:1 | 25.0% |
| 4:1 | 20.0% |
| 5:1 | 16.7% |

## ATH rule

At or near all-time highs there is no overhead supply by definition → no live
opposing zone → no long target → **no long entry** (that is the mid-rally chase).
Shorting fights the HTF trend with no basis. Action: **WATCH**; wait for a fresh
base (RBR pullback) to form and hold, then re-scan.

## Direction matrix — curve location × ITF trend

> ⚠️ **DRAFT — RECONSTRUCTED, NOT CONFIRMED.** Carried over from
> deep-dive-swing, where it is also flagged draft. It was reconstructed from the
> Seiden/OTA framework and past verdicts (ORCL, NFLX, TQQQ, CVX), **not** from
> Kenneth's OTA card. All three SHORT cells are inferred. State the cell applied
> and repeat this warning in any run that produces a short, so drift gets caught.

Curve location = where price sits between the nearest live **weekly** demand
(bottom) and nearest live **weekly** supply (top).

| | ITF Uptrend | ITF Sideways | ITF Downtrend |
|---|---|---|---|
| **Low on curve** | **BUY** at proximal — best long cell | **BUY** at proximal w/ confirmation | **BUY only on zone hold** — counter-ITF; LOW-CONVICTION if pass-2 |
| **Mid curve** | WATCH — no entry without chasing | **NO TRADE** — no edge either side | WATCH — wait for arrival at demand |
| **High on curve** | **SHORT** at proximal w/ confirmation (counter-ITF) | **SHORT** at proximal | **SHORT** at proximal — best short cell |

Degenerate cases:
- **Zero live supply:** long has no target → long capped at WATCH; short inapplicable.
- **Zero live demand:** short has no target → short capped at WATCH.

The matrix chooses *direction*. The gates decide *eligibility*. Every cell is
still subject to every gate above.
