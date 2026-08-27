#!/usr/bin/env python3
"""
fetch_240m.py — build a true 240-minute (4H) OHLC CSV for the LTF zone scan.

Yahoo has NO native 4h/240m interval, so we pull 60m bars and resample.
Yahoo caps 60m history at ~730 days; for 4H swing zones the useful window is
the last ~4-8 months. Default = 6mo.

Usage:
    python fetch_240m.py --ticker NOW [--period 6mo] [--out /tmp/NOW_240m.csv]

Then feed the CSV to the scanner:
    python zone_scanner.py --csv /tmp/NOW_240m.csv --timeframe 240min

Single unofficial feed (Yahoo) — every level must be cross-checked on
TradingView before Kenneth saves an alert or acts.
"""
import argparse, sys
import pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--period", default="6mo",
                    help="60m lookback (Yahoo max ~730d; 4H swing default 6mo)")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    out = a.out or f"/tmp/{a.ticker}_240m.csv"

    try:
        import yfinance as yf
    except ImportError:
        sys.exit("yfinance not installed: pip install yfinance --break-system-packages")

    h = yf.Ticker(a.ticker).history(period=a.period, interval="60m")
    if h is None or len(h) == 0:
        sys.exit(f"No 60m data returned for {a.ticker}")

    # Resample to true 240-minute bars. Uses the exchange-local tz Yahoo returns.
    agg = {"Open": "first", "High": "max", "Low": "min",
           "Close": "last", "Volume": "sum"}
    df = h.resample("240min").agg(agg).dropna(subset=["Open", "High", "Low", "Close"])
    df.index.name = "Date"
    df[["Open", "High", "Low", "Close", "Volume"]].to_csv(out)

    print(f"240m bars: {len(df)}  |  {df.index.min()} -> {df.index.max()}")
    print(f"last close: {df['Close'].iloc[-1]:.2f}")
    print(f"saved: {out}")

if __name__ == "__main__":
    main()
