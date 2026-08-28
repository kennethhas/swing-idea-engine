# The Continuation Override

**Status: DEFAULT entry model for the daily run.** The zone model is still correct
analysis; it is no longer the default *entry*.

## Why it exists

The zone model puts entry at demand, 5–15% under spot. In a trending tape those
limits frequently never fill — the name continues without you, and the screen has
technically "worked" while producing no trade. Kenneth's standing instruction:

> "I keep missing swings by waiting for discounts that never fill."

So the daily run asks a different question. Not *"where would I love to buy this?"*
but ***"what alert do I set so I am IN when it goes?"***

## The rule

**Entry is a trigger LEVEL ABOVE price** — the nearest overhead resistance the name
must reclaim to continue. Specifically one of:

- a **reclaim-close above the last lower-high** (the name pulled back, bounced to a
  lower high, and is coiling under it), or
- a **higher-low base holding** under a shelf (the name is at/near highs and coiling
  under the last swing high).

**Never a demand-zone limit below price.** A setup whose only entry is a deep discount
is CUT from the daily run, not listed. If the analysis is genuinely zone-shaped and
worth saying, it goes in the notes — never in Table 1 as an entry.

## The no-chasing counterweight

"Buy above price" degenerates into chasing without a hard ceiling on extension. Two
gates, both hard cuts:

- close ≤ **2.2 ATR** above the 20-day SMA
- close ≤ **12%** above the 50-day SMA

A name that is already vertical is CUT even if its structure is otherwise perfect.
This is the gate that removed ICE (+12.5% vs 50-day), MRK (+21%, ATR percentile 0.98),
ABBV, SCHW, EOG and CVX from the 2026-08-26 run. Expect it to cut the most exciting-
looking names on any strong day. That is the gate working, not misfiring.

## Gate order

Run in this order; the first failure is the cut reason.

| # | Gate | Threshold |
|---|---|---|
| 1 | Confirmed uptrend | close > SMA100, SMA50 ≥ SMA100, close within 6% of SMA50 |
| 2 | Not extended | ≤ 2.2 ATR over SMA20 **and** ≤ 12% over SMA50 |
| 3 | Contraction present | ATR percentile ≤ 0.75 **or** range-compression < 1.15 |
| 4 | Trigger reachable | nearest overhead level ≤ 10% above spot |
| 5 | Stop sane | 0.8 ≤ (trigger − stop) / ATR ≤ 3.0 |
| 6 | Reward sufficient | R:R to T1 ≥ 2.0 (see the deviation note) |

**Trigger** = `min()` of the pivot highs above spot in the last 70 sessions, plus the
10- and 20-day highs. The *nearest* wall, never the highest — taking the most recent
pivot instead pushed BAC's stop to 3.7 ATR in an earlier revision.

**Stop** = most recent swing low (k=2 pivots, last 25 sessions), floored by the last
three bars' low, minus 0.25 ATR.

## Target model — and the two ways it goes wrong

**T1 = highest CLOSE of the last 120 sessions + 0.5 ATR.** T2 = T1 + base height.
If the trigger already sits above that prior high (name at highs), T1 = trigger +
base height instead.

Two failure modes, both of which produced wrong numbers before being fixed:

1. **Measured move alone caps R:R near 1 by construction.** If the target is the base
   height projected up and the stop is the base low, reward and risk are the same
   distance. The prior high has to supply the room.
2. **Highest HIGH inflates R:R.** Several names' highs are single-bar rejection wicks —
   UNH's 461.62 closed 38 points off its high. Using the highest *close* is the fix,
   and there is a regression test pinning it.

## The R:R gate deviation — state it in every report

The zone model gates at **3:1**. Continuation entries carry a tighter stop *and* a
nearer ceiling, so a 3:1 gate returns an **empty table** in most tapes. The daily run
gates at **2:1** and prints the raw R:R for every name so the reader can impose their
own bar.

This is a deliberate, disclosed deviation from `gates-and-scoring.md`, not an
oversight. Say so once per report, in the footer. If a run is unusually rich, tighten
with `--min-rr 3.0` and say that instead.

## Core score (continuation-adapted, /9)

| Component | 2 points | 1 point | 0 |
|---|---|---|---|
| Room to run | <4% over SMA50 | <7% | ≥7% |
| Reward | R:R ≥ 3 | R:R ≥ 2 | — |
| Trend structure | above SMA100 with SMA50 > SMA100 | otherwise | — |
| Higher-low intact | yes | — | no |
| Coil | ATR pctl ≤ 0.35 or range-comp ≤ 0.85 | — | otherwise |

Tier: **A** = score ≥ 8 and R:R ≥ 3 · **B** = score ≥ 6 · **C** = passed but marginal.

## What the trader actually does with the output

The trigger is **where the alert goes**, not a market order. Take it on a **close
above** the trigger — not an intraday poke — ideally on expanding volume. The stop
goes under the marked higher-low the same session. State this once per report.

## Running it

```bash
python scripts/continuation_scan.py --csv-dir work/csv --show-cuts
python scripts/continuation_scan.py --csv-dir work/csv --min-rr 3.0 --json out.json
```

Input is a directory of `<SYMBOL>.csv` files with `Date,Open,High,Low,Close`. **Every
bar must be a completed session retrieved from a live feed this session.** The hard
rule from `SKILL.md` applies with no exception: a partially-retrieved bar (close known,
OHLC not) is `NA` and the row is dropped — never estimated. This has been violated once
and caught; it is the single most damaging failure mode in the whole chain.

## What this does NOT change

- Step 0 regime gate still runs and still re-weights.
- The squeeze/coil readiness layer still runs — gate 3 is the same idea, applied as a cut.
- The earnings-buffer gate still applies (no entry with earnings inside 5 trading days).
- Table 2 (off-the-radar discovery) is untouched — different horizon, different evidence.
- Single-ticker deep dives are a separate skill and still use zone entries unless the
  user asks otherwise.

---

## Appendix — measuring O.E. "Strength" (pinned 2026-08-28)

Reference Card 2 says the move-out leg and the structure break must each be
"≥2:1" but never names the denominator. That gap caused a live flip-flop: BAC was
scored 1/2, then 2/2, then back to 1/2 in one session, purely because the
denominator changed. Pinning it here so it cannot drift again.

**Use ATR at the formation bar. Never zone width.**

Zone width is unstable: a narrow base makes every departure look explosive. The
four zones measured on 2026-08-27 data:

| Ticker | Zone width | Width ÷ ATR | move-out ÷ width | move-out ÷ ATR |
|---|---|---|---|---|
| CSCO | 0.55 | **0.26** | **14.1** | 3.6 |
| AAPL | 5.19 | 0.62 | 4.1 | 2.5 |
| XOM | 3.31 | 0.83 | 2.1 | 1.7 |
| BAC | 1.04 | 0.88 | 2.0 | 1.7 |

CSCO's zone is a quarter of an ATR wide, so dividing by it returns 14:1 for a
departure that is 3.6 ATR — and 49:1 on a 5-bar window. Any measure that can
report 49:1 is measuring the denominator, not the move. ATR is scale-stable
across price levels and volatility regimes; use it.

**The measurement, exactly:**

- **move-out** = (highest high within 3 bars of the formation bar − proximal) ÷ ATR
  at the formation bar. Passes at ≥ 2.0.
- **structure break** = the post-formation high (30 bars) exceeds the highest
  swing-pivot high of the 40 bars before formation. Binary.
- Both pass → 2 · one → 1 · neither → 0.

This is still a chosen denominator, not the card's — say so in every report, and
show the raw ratio so the reader can overrule the category. It is the same class
of error as the T2 base-height bug fixed earlier the same day: a ratio taken
against a window that did not mean what it was assumed to mean.
