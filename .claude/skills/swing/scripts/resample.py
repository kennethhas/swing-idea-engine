#!/usr/bin/env python3
"""
resample.py — build the higher timeframes the three-layer read needs.

  daily  -> weekly  (HTF curve context)
  60m    -> 240min  (the LTF the entry comes off; "true 4H", so 4 one-hour bars
                     per bucket anchored to the session, NOT a wall-clock grid)

The LTF matters most: deep-dive-swing takes zones and entries from the 240min and
never from the weekly, so a sloppy 4H build corrupts every level downstream.

Usage:
    python3 resample.py --mode weekly --in csv/daily/CRM.csv --out csv/weekly/CRM.csv
    python3 resample.py --mode 240min --in csv/60m/CRM.csv  --out csv/ltf/CRM.csv
"""

import argparse
import csv
import datetime
import sys


def read(path):
    out = []
    for r in csv.DictReader(open(path)):
        out.append({"Date": r["Date"], "o": float(r["Open"]), "h": float(r["High"]),
                    "l": float(r["Low"]), "c": float(r["Close"]),
                    "v": float(r.get("Volume") or 0)})
    return sorted(out, key=lambda r: r["Date"])


def agg(bucket):
    return {"Date": bucket[-1]["Date"], "o": bucket[0]["o"],
            "h": max(b["h"] for b in bucket), "l": min(b["l"] for b in bucket),
            "c": bucket[-1]["c"], "v": sum(b["v"] for b in bucket)}


def key_weekly(r):
    d = datetime.date.fromisoformat(r["Date"][:10])
    return d - datetime.timedelta(days=d.weekday())        # Monday of that week


def main():
    p = argparse.ArgumentParser(description="Resample bars to weekly or true 240min.")
    p.add_argument("--mode", required=True, choices=["weekly", "240min"])
    p.add_argument("--in", dest="src", required=True)
    p.add_argument("--out", dest="dst", required=True)
    a = p.parse_args()

    bars = read(a.src)
    if not bars:
        sys.exit(f"no bars in {a.src}")
    out = []

    if a.mode == "weekly":
        cur_key, bucket = None, []
        for b in bars:
            k = key_weekly(b)
            if cur_key is not None and k != cur_key:
                out.append(agg(bucket))
                bucket = []
            cur_key = k
            bucket.append(b)
        if bucket:
            out.append(agg(bucket))
    else:
        # True 4H: group 4 consecutive 60m bars WITHIN a session. Starting a new
        # bucket at each session boundary is what keeps the 4H bars aligned to the
        # cash open instead of drifting across days.
        cur_day, bucket = None, []
        for b in bars:
            day = b["Date"][:10]
            if day != cur_day:
                if bucket:
                    out.append(agg(bucket)); bucket = []
                cur_day = day
            bucket.append(b)
            if len(bucket) == 4:
                out.append(agg(bucket)); bucket = []
        if bucket:
            out.append(agg(bucket))   # partial trailing bar, flagged by the caller

    with open(a.dst, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Date", "Open", "High", "Low", "Close", "Volume"])
        for r in out:
            w.writerow([r["Date"], round(r["o"], 4), round(r["h"], 4),
                        round(r["l"], 4), round(r["c"], 4), int(r["v"])])
    print(f"{a.src}: {len(bars)} bars -> {len(out)} {a.mode} bars -> {a.dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
