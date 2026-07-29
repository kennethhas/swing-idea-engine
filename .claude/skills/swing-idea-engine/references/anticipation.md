# The Anticipatory Layer — screening for the swing before it happens

This is what makes the engine forward-looking. Read it whenever you run Task A. The zone
scanner answers "where could a swing start?"; this layer answers "which names are about to
move, and has the move begun?"

## The sequence: Regime → Coil → Level → Trigger

A high-quality anticipatory setup fires these in order. The more that align, the higher the
conviction. Missing the later ones isn't fatal — it just means "watch," not "act."

1. **Regime (Step 0)** — is the broad tape supportive for the direction?
2. **Coil (Step 1 squeeze scan)** — is the name contracting (energy building)?
3. **Level (Step 2 zone scan)** — is there a defensible, gated zone at hand?
4. **Trigger (Step 2 entry rule)** — has price actually started to reclaim/expand?

Reactive screening jumps straight to "it's moving, chase it." This layer front-runs that.

## 1. Regime gate — `regime_gate.py`

```bash
python scripts/regime_gate.py --symbols SPY,QQQ        # add ,SOXX for semis-heavy runs
```

Reports each index's posture vs its 50/200 SMA and 20-day range, then a combined verdict:
- **GREENLIGHT** — all constructive; longs with-regime.
- **SELECTIVE / MIXED** — longs lower-odds; demand better zones + tighter risk.
- **CAUTION / BEARISH** — tag longs COUNTER-REGIME; favor shorts.

It re-weights, never cuts. A great setup counter-regime is still shown — just flagged.

## 2. Squeeze / coil scan — `squeeze_scan.py`

```bash
python scripts/squeeze_scan.py --tickers SYM1,SYM2,... --min-score 0
```

0–100 **readiness** from four contraction signals + trend posture:

| Signal | Coiled looks like | Why it's leading |
|---|---|---|
| Volatility contraction (ATR% percentile) | ATR% in bottom quartile of its 6-mo range | Quiet precedes violent; low vol mean-reverts to high |
| Bollinger squeeze (BB-width percentile) | Width in bottom quartile | Bands pinch before expansion moves |
| Range compression (recent band vs prior) | ratio < ~0.8 | The tape is tightening in real time |
| Volume dry-up (10d vs 50d avg) | ratio < ~0.8 | Sellers exhausted / quiet accumulation |
| Trend posture (50/200 + price) | context only | Coil in an uptrend favors an up-swing |

Bands: **COILED ≥70**, **TIGHTENING 55–69**, **NEUTRAL 40–54**, **EXPANDED <40**.

Readiness does NOT replace zone gates. It orders the queue and adds conviction when it
agrees with a fresh gated zone. When squeeze and zone disagree (e.g. a name cut on R:R but
reading COILED), surface both — that disagreement is signal, not noise.

Interpretation caveats:
- Coiled names can stay coiled, or release the "wrong" way. Readiness ranks probability of
  *a move*, not its direction — direction comes from the zone + regime.
- A name can read COILED because it's dead (no participation), not because it's loading.
  Cross-check that there's a real catalyst path (earnings ahead, sector flow) before calling
  it primed.
- Needs ≥60 daily bars; returns NA below that (mirrors the min-history rule elsewhere).

## 3. Multi-timeframe (Step 2)

Weekly zone = context, daily zone = trigger. A daily demand zone sitting inside a weekly
demand zone with a weekly uptrend is the "big picture" enhancer at full marks. A daily zone
fighting weekly supply overhead is usually a cut, however clean it looks on the daily.

## 4. Entry trigger (Step 2)

The zone is *where*; the trigger is *when the swing starts*. Two modes:
- **Confirmation entry** (default in SELECTIVE/CAUTION): wait for the reclaim close back
  through the proximal on expanding volume. Borrow the Body-Closure/confirmation logic from
  asymmetric-reclaim-analyst.
- **Limit-in entry** (GREENLIGHT + fresh high-score zone only): resting order at proximal,
  accepting first-touch risk.

State which applies per name. "Coiled + gated zone + reclaim printed" = the full sequence;
that's the top-of-table setup.

## Honest limits of the anticipatory layer

- It shifts the odds earlier; it does not predict. False positives (coil that fizzles) are
  expected and are why the trigger step exists.
- All contraction math runs on one unofficial feed for history — cross-check the latest
  close with `scripts/data_sources.py` (Yahoo vs CNBC, independent providers) before
  capital. A DIVERGE verdict usually means an unadjusted split or a bad print; resolve it
  before trading the level. Note: Stooq's keyless CSV, the usual second source, is now
  behind a JS/bot wall from server environments (verified Jul 2026), which is why CNBC is
  the corroborating feed.
- Earnings is the most common swing catalyst yet the earnings buffer excludes those names.
  That's a deliberate gap-risk tradeoff; if Kenneth wants earnings-driven swings, that's a
  separate mode with explicit gap-risk handling, not this default.
