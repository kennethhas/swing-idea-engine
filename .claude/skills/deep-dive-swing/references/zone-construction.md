# Zone Construction Reference

How to find a zone, classify it, and draw its boundaries. Read this before marking any chart or trusting scanner output.

## Table of contents
1. The base and the leg-out
2. The four patterns in detail
3. Drawing proximal and distal lines
4. Wick-inclusive vs body-only (the entry/risk trade-off)
5. Scanning order and common mistakes

---

## 1. The base and the leg-out

Every zone has two parts:

- **Base** — a small pause or consolidation: a cluster of small-range candles where price went sideways before exploding. This is where unfilled institutional orders are assumed to rest. Ideal base = **1-3 candles**; treat anything over ~6 candles as a weak or invalid base (too much time = equilibrium, not imbalance).
- **Leg-out (departure)** — the explosive move away from the base. A valid leg-out is **clearly larger than the base candles** — a useful rule of thumb is the leg-out's first decisive move is at least ~3x the height of the base. A weak, drifting departure means little imbalance and a low-quality zone.

The cleaner and smaller the base, and the more violent the leg-out, the stronger the zone. These two observations drive the "Strength" and "Time at level" enhancers.

**Basing candle definition:** the *last* small candle before the explosive move is the critical one — it marks the final price where the institution could fill orders. It can be bullish or bearish; color doesn't matter, range does.

---

## 2. The four patterns in detail

Read the sequence of legs *into* and *out of* the base.

### Demand zones (look to buy on return)
- **DBR — Drop · Base · Rally** (reversal). Price was falling, paused, then rallied hard. Turns a downtrend up. Usually the strongest demand because reversing a trend takes the most capital.
- **RBR — Rally · Base · Rally** (continuation). Uptrend pauses, then resumes up. A low-risk re-entry into an existing uptrend.

### Supply zones (look to sell on return)
- **RBD — Rally · Base · Drop** (reversal). Price was rising, paused, then dropped hard. Turns an uptrend down. Usually the strongest supply.
- **DBD — Drop · Base · Drop** (continuation). Downtrend pauses, then resumes down. A low-risk re-entry into an existing downtrend.

**Reversal (DBR/RBD) vs continuation (RBR/DBD):** reversal zones generally earn more "Big Picture / Strength" credit because the imbalance needed to flip direction is larger. But a continuation zone *aligned with a strong trend* can be higher-probability for a trade even if the raw imbalance is smaller — trend is on your side. Weigh both; don't auto-rank reversals first.

---

## 3. Drawing proximal and distal lines

- **Proximal line** = the zone edge **closest to current price**. This is the entry edge.
- **Distal line** = the zone edge **furthest from current price** (the extreme). This is the stop-loss edge.

### Demand zone
- **Proximal** = the **top of the base** (the high of the basing candles' bodies, or the highest wick if drawing wick-inclusive).
- **Distal** = the **lowest point of the base** (lowest wick / the swing low under the base).
- Entry on a touch of proximal; stop just below distal.

### Supply zone
- **Proximal** = the **bottom of the base** (the low of the basing candles' bodies, or the lowest wick if wick-inclusive).
- **Distal** = the **highest point of the base** (highest wick / the swing high above the base).
- Entry on a touch of proximal; stop just above distal.

Always **extend the zone horizontally to the right** so future price interacts with it. Report both lines as actual price levels.

---

## 4. Wick-inclusive vs body-only (the entry/risk trade-off)

There is no single "correct" boundary — it's a deliberate trade-off, and you should state which you used:

- **Wick-inclusive (bodies + wicks):** wider zone. Larger stop, but a higher chance the order fills because the zone reaches further into price. More conservative on fills, less efficient on risk.
- **Body-only (ignore wicks):** tighter zone. Smaller stop and better reward:risk, but price may reverse before reaching the proximal and you miss the fill.

Default to **body-for-proximal, wick-for-distal** as a balanced construction (tighter entry, protective stop beyond the extreme), and note that the alternative exists. When the wick is unusually long, flag that the two methods diverge materially and show both stops.

---

## 5. Scanning order and common mistakes

**Scan right-to-left from current price.** Start at the latest bar, look left/up for the nearest explosive drop (→ supply) and left/down for the nearest explosive rally (→ demand) *without cutting through intervening candles*. The first clean base behind each leg-out is the nearest live zone. Continue outward for the next zones.

**Common mistakes to avoid (and flag if the user made them):**
- **Calling consolidation a zone.** A long sideways range with no explosive exit is equilibrium, not a zone. No leg-out → no zone.
- **Oversized base.** More than ~6 candles in the base means the imbalance has bled away; downgrade or reject.
- **Counting tested zones as fresh.** Each time price returns and reacts, resting orders get consumed. A twice-tested zone is weaker, not "proven."
- **Trading a broken zone.** Once price *closes through* a zone (a close below a demand zone's distal, or above a supply zone's distal), it is invalidated — the orders are gone and the level often flips to act as the opposite (broken demand → resistance, broken supply → support). A wick through is a test; a close through is death. Don't plan entries at invalidated zones.
- **Ignoring timeframe.** Mark the zone on the timeframe it formed on; a higher-timeframe zone overrides a lower-timeframe one in the same area.
- **Drawing from the wrong candle.** The base is the *last small candle(s) before* the move, not the big momentum candle itself.
