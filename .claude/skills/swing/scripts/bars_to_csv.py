#!/usr/bin/env python3
"""
bars_to_csv.py — turn one combined bar dump into per-symbol CSVs the scanners read.

Why this exists: the skill's own feeds are egress-blocked in cloud sessions, so
Claude retrieves bars through the Massive MCP server and the oversized result is
spilled to a file on disk. That file never passes through context, which is what
makes a wide scan affordable. This converts it.

Accepts either:
  * the raw {"result": "<csv text>"} JSON a saved MCP tool result contains, or
  * a plain CSV with a leading `ticker` column.

Expected columns: ticker,Date,Open,High,Low,Close,Volume

Usage:
    python3 bars_to_csv.py dump.txt --out-dir csv/daily
    python3 bars_to_csv.py dump.txt --out-dir csv/ltf --timeframe 240min
"""

import argparse
import csv
import io
import json
import os
import sys

NEEDED = ["Date", "Open", "High", "Low", "Close"]


def load_text(path):
    raw = open(path, encoding="utf-8").read()
    s = raw.lstrip()
    if s.startswith("{"):
        try:
            return json.loads(raw)["result"]
        except (ValueError, KeyError) as e:
            sys.exit(f"{path} looks like JSON but has no usable 'result' string: {e}")
    return raw


def main():
    p = argparse.ArgumentParser(description="Split a combined bar dump into per-symbol CSVs.")
    p.add_argument("dump")
    p.add_argument("--out-dir", required=True)
    p.add_argument("--timeframe", default="daily", help="label only, for the log line")
    a = p.parse_args()

    rows = list(csv.DictReader(io.StringIO(load_text(a.dump))))
    if not rows:
        sys.exit("no rows parsed from the dump")
    cols = rows[0].keys()
    if "ticker" not in cols:
        sys.exit(f"dump needs a 'ticker' column; found {list(cols)}")
    missing = [c for c in NEEDED if c not in cols]
    if missing:
        sys.exit(f"dump missing required column(s): {missing}")

    os.makedirs(a.out_dir, exist_ok=True)
    by = {}
    for r in rows:
        by.setdefault(r["ticker"], []).append(r)

    for sym in sorted(by):
        bars = sorted(by[sym], key=lambda r: r["Date"])
        path = os.path.join(a.out_dir, f"{sym}.csv")
        with open(path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
            for r in bars:
                w.writerow([r["Date"], r["Open"], r["High"], r["Low"],
                            r["Close"], r.get("Volume", 0) or 0])
        print(f"{sym}: {len(bars)} {a.timeframe} bars -> {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
