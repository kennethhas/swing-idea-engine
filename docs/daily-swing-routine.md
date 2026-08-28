# Daily Swing Routine — runbook

The scheduled routine's prompt should be short and point here, so the procedure can be
edited in git instead of in the app. Canonical one-liner for the routine prompt:

> Run the daily swing routine per `docs/daily-swing-routine.md` in the swing-idea-engine
> repo. Continuation override is in force. Notify me only if Table 1 is non-empty or the
> run failed.

---

## What this run is

**A continuation-trigger screen.** Entries are alert levels *above* spot that a trending
name must reclaim. Not discount limits below spot — those frequently never fill and the
trend leaves without us. Spec: `.claude/skills/swing-idea-engine/references/continuation-override.md`.

## Procedure

**0 · Regime.** Establish the tape's posture (SPY/QQQ, add SOXX for semis-heavy runs).
It re-weights; it never cuts a name by itself. Record it in the report header.

**1 · Universe.** Reuse `work/csv/` (the cached OHLC set) and refresh every symbol to the
last completed session. Add names only for a reason worth stating. Liquidity floor:
price > $10, avg volume > 1M shares.

**2 · Data.** Pull daily OHLC per symbol into `work/csv/<SYMBOL>.csv` with header
`Date,Open,High,Low,Close`.

- **Feed: Massive (Polygon).** Yahoo, Stooq, CNBC and nasdaq are all blocked by the
  egress proxy, so the skill's bundled fetchers (`zone_scanner.py --ticker`,
  `data_sources.py`) cannot reach the network. Use the CSV path. FMP MCP works for a
  subset of symbols and is the cross-check where available.
- **Never synthesize a bar.** If only the close came back, the row is `NA` and gets
  dropped. A partially-known bar has been fabricated once in this repo's history and
  caught; treat the rule as absolute.
- Rate limits are real (~2–3 Massive calls/60s, workspaces expire). Pace the refresh.

**3 · Screen.**

```bash
python3 .claude/skills/swing-idea-engine/scripts/continuation_scan.py \
  --csv-dir work/csv --show-cuts --json work/continuation_$(date +%F).json
```

**4 · Earnings gate.** For every survivor, confirm no earnings inside 5 trading days.
Mark calendar-verified dates as verified and **inferred** dates as inferred — an earnings
date guessed from an earnings-shaped reversal bar is inference, and must say so.

**5 · Report.** Write `reports/swing_continuation_<date>.md`:

- **Table 1 — setups.** Ticker | Spot | Entry = trigger | Δ to trigger | Stop | Risk |
  Stop ×ATR | T1 | R:R | T2 | Core | Tier | Earnings in window. **Every entry above spot**
  — if one isn't, it doesn't belong in the table.
- One-line thesis per name. Trigger mechanics stated once: take it on a **close above**
  the trigger, not an intraday poke; stop under the marked higher-low the same session.
- **Table 2 — the cut log**, with the number that caused each cut, grouped by reason,
  plus a line on what the pattern says about the tape.
- **Footer, mandatory:** the 2:1 R:R deviation from the zone model's 3:1 · the target
  model (highest *close* of 120 sessions + 0.5 ATR) · single-feed caveat and
  "re-verify on TradingView" · which earnings dates are inferred · levels expire at the
  next open · not financial advice · confidence 0–1.

**6 · Commit** the report to `claude/awesome-galileo-opbb9l` and push.

## Notification policy

This runs unattended, so the notification *is* the deliverable — but a ping that says
"ran, found nothing" is worse than silence.

- **Notify** when Table 1 is non-empty (lead with the tickers and their trigger levels),
  or when the run **failed** — data feed unreachable, scanner error, nothing refreshed.
- **Stay silent** on a clean empty run. An empty Table 1 is a valid, honest output; log
  it in the report and say nothing.

## Standing rules that do not change

- An empty table is a valid output. Never pad the list to hit a count.
- A name failing any gate is **CUT, not downgraded**.
- Every price traces to data retrieved this session. No recall, no interpolation.
- Label fact vs. inference; flag discrepancies rather than silently resolving them.
- Not financial advice — sizing and the decision are the trader's.

## Known gaps

- **Universe breadth.** `work/csv/` is ~43 names accumulated from ad-hoc screens, tilted
  toward energy, defense, financials and AI-infra. It is not a systematic universe. Widen
  it deliberately, and say in the footer what the universe actually was.
- **Cross-feed verification** is unavailable for most symbols (FMP plan limits), so most
  levels are single-feed. Say so once per report.
- **Off-the-radar discovery (Table 2 of the skill)** is not part of the daily run — it
  needs a different universe (cap band $300M–$8B, ≤12 covering analysts) and a 3–5 year
  horizon. Run it on request, separately.
