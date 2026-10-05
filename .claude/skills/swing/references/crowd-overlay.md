# Crowd overlay — TipRanks and Stocktwits

## The one rule that matters

**Crowd data is a ±1 modifier. It can never admit a name, and it can never
override a gate.** If sentiment is allowed to *create* a setup, this stops being a
zone-gated system and becomes a momentum chaser — the exact failure mode the
engine exists to avoid. The zone decides; the crowd is read *against* it.

## Reading it

| State | Read | Modifier |
|---|---|---|
| Extreme bullish crowd **+ price at supply** | the crowd is the exit liquidity — best short context | **+1** |
| Extreme bullish crowd **+ fresh demand after a pullback** | confirms interest, nothing more | **0 / +1** |
| Extreme bullish crowd **+ price extended, no zone** | crowded long, nothing to do | **−1** |
| Extreme bearish crowd **+ price at demand** | capitulation into a level — best long context | **+1** |
| Extreme bearish crowd **+ price at supply** | agrees with the short, adds little | **0** |
| TipRanks Strong Buy, target far above spot | already priced in — a crowding signal, not a reason | **−1 / 0** |

The most valuable TipRanks fields are **not** the star rating. They are:
1. **the next earnings date** — feeds the 5-day buffer gate directly
2. **recent rating changes** — a dated catalyst

Weight the consensus score least. It is the most crowded, least timely number on
the page.

## Getting the data

Both sites are blocked by the cloud session's egress proxy (`api.stocktwits.com`,
`stocktwits.com`, `www.tipranks.com` all return EGRESS_BLOCKED), and FMP's
TipRanks route is a paid add-on that no subscription tier includes. So:

1. **Preferred — the user's own browser.** Run from the desktop app or a linked
   device and read both sites through `chrome-browser` / `built-in-browser`, which
   act in their real browser with their sign-ins. This is the only free structured route.
2. **Fallback — WebSearch.** Works from cloud, returns unstructured text. Fine for
   an earnings date or a rating change; poor for a sentiment score.
3. **Fallback — pasted values.** Accept numbers the user pastes.

Whichever route is used, **record it per name.** A crowd read whose source is
unstated is not evidence. If no route is available, run with `--crowd 0` and say
the overlay was skipped rather than guessing a sentiment.
