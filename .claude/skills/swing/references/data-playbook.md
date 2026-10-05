# Data playbook — no FMP, no Yahoo, one price vendor

## What is actually reachable (verified 2026-10-05)

| Source | Status | Use |
|---|---|---|
| **Massive / Polygon MCP** | ✅ works, free tier | **the price engine** — all OHLCV, every timeframe |
| **WebSearch** | ✅ works | earnings dates, catalysts, rating changes |
| `chrome-browser` / `built-in-browser` | ✅ on desktop / linked device | TipRanks, Stocktwits |
| Yahoo (`query1/2.finance.yahoo.com`) | ❌ EGRESS_BLOCKED | — |
| FMP `chart` / `quote` / `news` | ❌ plan-gated | — |
| FMP `tipranks` | ❌ paid add-on, no tier includes it | — |
| Massive Benzinga / TMX earnings | ❌ NOT_ENTITLED on free tier | — |
| Bigdata.com | ❌ credits exhausted | — |
| stooq, nasdaq, stockanalysis, polygon.io, cnbc direct | ❌ all EGRESS_BLOCKED | — |

**Do not retry the blocked routes.** They are organization egress policy or plan
entitlement, not transient failures.

## Consequence: every level is SINGLE-SOURCE

The cross-feed check (`data_sources.py`) cannot run. State this in every output.
Two partial mitigations, and be precise about what each proves:

- **Vendor-internal consistency** — compare per-ticker aggregates against the
  grouped-daily snapshot. Catches splits, unadjusted series and bad prints. It is
  **consistency, not corroboration** — same vendor, so it is not independence.
- **WebSearch spot-check** — verify the close for the 1–5 survivors only. Semi-independent, enough to catch a badly wrong level.

Tag every level `ONE-SOURCE — verify on TradingView before order entry`.

## The cache is the whole trick

Polygon's grouped-daily endpoint returns **every US ticker's bar for one date in a
single call** (~12,600 rows). So:

```
/v2/aggs/grouped/locale/us/market/stocks/{date}   # 1 call = whole market, 1 day
```

- **Daily maintenance: one call.** The ~5-calls-per-minute free-tier limit stops mattering.
- Screen the **whole market** instead of a hand-guessed universe.
- Runs become reproducible instead of re-fetched.
- Seeding costs one backfill session (~60 grouped calls, paced).

Per-ticker history, only for names that survive the coil screen:

```
/v2/aggs/ticker/{SYM}/range/1/day/{from}/{to}     # ITF daily  (2y)
/v2/aggs/ticker/{SYM}/range/1/week/{from}/{to}    # HTF weekly (5y)
/v2/aggs/ticker/{SYM}/range/4/hour/{from}/{to}    # LTF 240min (~6mo)
```

If the 4H endpoint is thin or unavailable, pull `1/hour` and build true 4H with
`scripts/resample.py --mode 240min`, which anchors buckets to the session rather
than to a wall-clock grid.

## Moving bars without burning context

A `query_data` result that exceeds the token ceiling is **spilled to a file on
disk** and the tool returns that path. That file never passes through context —
which is what makes a wide scan affordable. Use it deliberately:

1. `call_api` with `store_as` to land bars in the workspace (server side).
2. `query_data` a combined `SELECT ticker, Date, Open, High, Low, Close, Volume`
   across every stored table — let it overflow.
3. Feed the saved path to `scripts/bars_to_csv.py`.

Do **not** paste bar data back through a heredoc; that doubles the cost of the one
thing you were trying to avoid paying for once.

## Rate limiting

Free tier refills slowly — roughly 4–5 `call_api` calls per window, and the window
is longer than a minute. Batch 4, then wait. `query_data` is local SQL and is not
rate limited, so push every transformation into SQL rather than into more calls.

## If you ever do pay

Spend it on **Massive, not FMP** — Massive is the engine. The one plugin that would
close the cross-feed gap, the earnings gap and part of the crowd layer in a single
move is **EODHD** (own MCP server, free tier exists). Evaluate that before buying
anything narrower.
