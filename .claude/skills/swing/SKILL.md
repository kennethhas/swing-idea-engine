---
name: swing
description: >
  Kenneth's end-to-end swing pipeline — the multi-name screener and the
  deep-dive gates in one chain, run with `/swing`. Inherits the deep-dive-swing
  horizon profile exactly (HTF Weekly = curve, ITF Daily = trend, LTF 240min =
  zones + entry) and the R:R >= 3:1 both-directions gate shared with
  surge-deep-dive. Runs Regime+breadth -> Coil -> three-timeframe zone read ->
  hard gates -> crowd overlay -> risk-normalized sizing -> memory -> trigger
  watch. Long AND short. Every price level traced to data retrieved this
  session, never recalled. Trigger on `/swing`, "run the swing pipeline",
  "swing scan", "what should I trade", or any multi-name swing request. For a
  single ticker use deep-dive-swing; to score one already-defined zone use
  surge-oe-scorecard.
---

# /swing — the zone-gated swing pipeline

## What this is

One chain from "screen the market" to "here is the size, logged." It exists
because the pieces already existed separately and nothing joined them: the
screener produced levels nobody sized, the sizing skill never saw the screener's
output, and no run was ever recorded, so the gates could never be calibrated.

**Operate as a critical reasoning agent throughout.** Label fact vs. inference.
Surface discrepancies instead of resolving them silently. **An empty table is a
valid, honest output** — never pad to hit a count. This is educational analysis,
**not financial advice**; the trade decision and the size are the user's.

Read `references/gates-and-matrix.md` and `references/data-playbook.md` at the
start of every run. Read `references/crowd-overlay.md` before touching stage 6.

## Non-negotiables

1. **No price level exists unless it was retrieved this session.** If it cannot be
   retrieved, write `NA`. Never estimate, recall or interpolate a level.
2. **The gates cut; they do not downgrade.** A name failing a hard gate is gone.
3. **Crowd data is a ±1 modifier.** It can never admit a name or override a gate.
4. **Levels expire at the next session's open.** Say so every time.
5. **Every level is single-source.** Tag it and say what that does not prove.

---

## STAGE 0 — Cache + regime + breadth

```bash
# bars come from Massive MCP (see data-playbook.md), then:
python3 ../swing-idea-engine/scripts/regime_gate.py \
    --csv SPY=csv/daily/SPY.csv --csv QQQ=csv/daily/QQQ.csv --symbols ""
```

Then compute sector breadth from the grouped-daily cache: 1m/3m/6m return for all
11 sector ETFs (XLE XLC XLY XLP XLK XLV XLRE XLB XLF XLU XLI) against SPY.

**Gate: index trend constructive AND ≥ 4 of 11 sectors positive on 1m.**

This gate exists because of a real false green: on 2026-10-02 SPY and QQQ were
both above their 50 and 200 DMA — a clean GREENLIGHT — while **only Technology was
positive on the month and 9 of 11 sectors were negative.** Index trend alone said
buy; breadth said the tape was being carried by one group. Report both, and let
breadth downgrade the verdict to SELECTIVE.

## STAGE 1 — Coil screen (anticipatory, not reactive)

```bash
python3 ../swing-idea-engine/scripts/squeeze_scan.py --csv csv/daily/<SYM>.csv --min-score 0
```

Carry forward **readiness ≥ 55** (TIGHTENING and COILED). Selecting on realized
momentum is lagging — by the time a name "shows momentum" part of the move is gone.

Two traps to check before calling a coil primed:
- **A name can read COILED because it is dead, not loading.** Cross-check that a
  catalyst path exists.
- **A deal-pinned stock reads as a perfect coil.** On 2026-10-05 AES showed ATR
  0.31% on a $14.91 stock with a $0.70 six-month range — that is an acquisition
  pin, not stored energy. Flag any name whose ATR% sits in the bottom few percent
  *and* whose range has collapsed, and check for a pending deal before trusting it.

## STAGE 2-4 — The three-layer read

| Stage | TF | Produces |
|---|---|---|
| 2 | **Weekly** (5y) | curve location: where price sits between nearest live weekly demand and supply |
| 3 | **Daily** (2y) | ITF trend: HH/HL vs LH/LL, SMA20/50 |
| 4 | **240min** (~6mo) | **the zone and the entry** |

```bash
python3 scripts/resample.py --mode weekly --in csv/daily/<SYM>.csv --out csv/weekly/<SYM>.csv
python3 scripts/resample.py --mode 240min --in csv/60m/<SYM>.csv  --out csv/ltf/<SYM>.csv
python3 ../swing-idea-engine/scripts/zone_scanner.py --csv csv/ltf/<SYM>.csv --timeframe 4h
```

A daily or 4H zone fighting weekly supply overhead is usually a cut however clean
it looks on the LTF. If the LTF scan finds nothing at the default `--leg-mult`,
a pass-2 run at `--leg-mult 1.3` may be used but the zone is tagged
**LOW-CONVICTION and capped at WATCH**.

The scanner is a **first pass**. Big Picture / Arrival / Curve need visual
confirmation — adjust scores you disagree with and say which and why.

## STAGE 5 — Direction, then the hard gates

Pick the cell from the matrix in `references/gates-and-matrix.md` (curve location ×
ITF trend) and **state which cell was applied**. The matrix chooses direction; the
gates decide eligibility.

> Any run producing a SHORT must repeat the matrix's DRAFT warning: the short
> cells are reconstructed, not from Kenneth's OTA card.

```bash
python3 scripts/gates.py --ticker CRM --direction long --price 234.69 \
    --proximal 209.17 --distal 198.95 --stop 197.93 \
    --target 253.62 --target-tf weekly \
    --odds 8 --tested 1 --bars-ltf 180 --earnings-days 42
```

Returns every gate PASS/FAIL with its detail, the R:R to the **actual stop**, and
the verdict `TRADE / WATCH / INELIGIBLE`. Use `--json` to chain it.

## STAGE 6 — Earnings, then the crowd overlay

Earnings first, because it is a gate and the crowd is not. Get the date from
`equity-research`'s `catalyst-calendar`, TipRanks via the user's browser, or
WebSearch. **An unverified date is treated as blocking** — `gates.py` fails the
earnings gate when `--earnings-days` is omitted, by design.

Then apply the crowd overlay per `references/crowd-overlay.md` and pass
`--crowd -1|0|1`. Record the source per name. No route available → `--crowd 0`
and say the overlay was skipped.

## STAGE 7 — Risk-normalized sizing

```bash
python3 scripts/size.py --entry 209.17 --stop 197.93 --target 253.62
python3 scripts/size.py --entry 209.17 --stop 197.93 --equity 50000 --risk-pct 1
```

Neither deep-dive-swing nor surge-deep-dive defines account size or risk %, so
**never assume one.** Default output is per-$10,000 of equity, valid at any size.

Quarter-Kelly and Monte Carlo risk-of-ruin need a measured win rate and avg
win/loss from **closed trades**. With no history they are dormant and sizing is
fixed-fractional; `size.py` says so rather than inventing a win rate, and refuses
to compute Kelly off fewer than 20 closed trades. Pair with **TradingCalc** for
deterministic position-size / VaR / Sharpe math.

## STAGE 8 — Record every idea, triggered or not

Log to `trader-memory-core`. This is the stage that makes the gates improvable: in
three months it is the only thing that can tell you whether 6/9 and 3:1 are too
loose, too tight, or right. A run that is not recorded teaches nothing.

## STAGE 9 — Watch the trigger

A zone says *where*, not *that the swing has started*. State the trigger per name:

- **Confirmation entry** (default in SELECTIVE/CAUTION): wait for a close back
  through the proximal on expanding volume.
- **Limit-in** (only in GREENLIGHT, on a fresh high-score zone): resting order at
  proximal, accepting first-touch risk.

Entries are frequently well below spot — a wait-level, not an at-market idea. Say
that plainly, and set the watch with `/loop` + Monitor rather than implying action
today.

---

## Output

**Table 1 — gated setups:** Ticker | Dir | Entry (proximal) | Stop | T1 (+TF) | T2 |
R:R | Odds | Coil | Matrix cell | Verdict | Trigger | Crowd | Shares/$10k @1% |
Data as-of

Sort by: verdict (TRADE first), then coil + with-regime alignment. A gated zone with
low readiness still lists, flagged "coil already released — level only."

**Table 2 — every name cut, with the one-line reason.** This is signal, not filler.
A rejected name with its reason is more useful than a forced pick.

**Footer (mandatory):**
- Count cut, each with reason
- Overall confidence 0–1, and what drives it up and down
- `ONE-SOURCE` data tag + what the missing cross-check does not prove
- Any DRAFT-matrix warning, if a short was produced
- Levels expire at next session's open; re-verify on TradingView; not financial advice

If fewer than 3 names survive, **say so plainly.** On 2026-10-05, 1 of 27 survived
— that was the honest answer and the breadth data explained it.

## Tests

```bash
python3 tests/test_gates.py        # 17 gate regressions, stdlib only
```

Run after any edit to `gates.py`. The suite pins the real CRM case (3.95:1 → TRADE)
and the real META case (price inside weekly supply → WATCH, not INELIGIBLE).

## Composition

- One named ticker → **deep-dive-swing**.
- One already-defined zone to score → **surge-oe-scorecard**.
- A liquidity-sweep-and-reclaim question → **asymmetric-reclaim-analyst**.
- A factual claim the user makes → **truth-engine**.
