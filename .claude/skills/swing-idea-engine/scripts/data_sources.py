#!/usr/bin/env python3
"""
data_sources.py — Second data source (CNBC) + cross-feed verification.

Why this exists
---------------
The zone/squeeze/regime scripts all fetch from ONE unofficial feed (Yahoo). A single
source is a real reliability hole: a bad Yahoo print (unadjusted split, spiked wick, stale
bar) silently becomes a "trade level." This adds an INDEPENDENT feed and a cross-check so a
level backed by two agreeing sources is trusted, and a divergence is FLAGGED before it
becomes a trade.

Source choice (documented, because it matters)
----------------------------------------------
Stooq's keyless CSV — the obvious pick — is now behind a JavaScript/bot wall from server
environments (returns a "requires JavaScript" stub, not data). Verified July 2026. So this
uses CNBC's keyless quote JSON, which comes from a DIFFERENT data provider than Yahoo and so
genuinely corroborates rather than echoing the same feed. CNBC gives a real-time/last quote
(latest close after hours), not deep history — exactly what a latest-close cross-check needs.
If CNBC is unavailable, the module says ONE-SOURCE honestly rather than faking agreement.

What it provides
----------------
- fetch_cnbc_quote(ticker) -> dict            (latest OHLC + last, independent of Yahoo)
- cross_check(ticker, tol_pct=1.0) -> dict    (compares latest close across both feeds)

Security: charset allowlist on the symbol; the fetchers only build known quote URLs for a
plain symbol and are not general URL tools. Treat all fetched data as untrusted input.
"""

import sys
import re

try:
    import requests
except ImportError:
    requests = None

try:
    from zone_scanner import fetch_yahoo, validate_bars
except ImportError:
    sys.path.insert(0, __file__.rsplit("/", 1)[0])
    from zone_scanner import fetch_yahoo, validate_bars


_ALLOWED = re.compile(r"[A-Za-z0-9.\-^=]{1,15}")


def fetch_cnbc_quote(ticker):
    """Latest quote from CNBC's keyless endpoint. Independent provider from Yahoo.
    Returns a dict with last/open/high/low/volume/prev_close/asof or raises SystemExit."""
    if requests is None:
        sys.exit("requests not available; cannot use CNBC source.")
    if not _ALLOWED.fullmatch(ticker or ""):
        sys.exit(f"Refusing suspicious ticker '{ticker}'.")
    url = ("https://quote.cnbc.com/quote-html-webservice/quote.htm"
           f"?symbols={ticker.upper()}&output=json")
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
        data = r.json()
    except Exception as e:  # noqa
        sys.exit(f"CNBC fetch failed for '{ticker}': {e}")
    try:
        q = data["QuickQuoteResult"]["QuickQuote"]
        q = q[0] if isinstance(q, list) else q
    except (KeyError, TypeError, IndexError):
        sys.exit(f"CNBC returned no quote for '{ticker}'.")

    def _f(key):
        v = q.get(key)
        try:
            return float(v)
        except (TypeError, ValueError):
            return None

    last = _f("last")
    if last is None:
        sys.exit(f"CNBC quote for '{ticker}' had no usable last price.")
    return {
        "symbol": q.get("symbol", ticker.upper()),
        "last": last,
        "open": _f("open"),
        "high": _f("high"),
        "low": _f("low"),
        "volume": _f("volume"),
        "prev_close": _f("previous_day_closing"),
        "asof": q.get("last_time") or q.get("reg_last_time"),
        "provider": q.get("provider"),
    }


def cross_check(ticker, tol_pct=1.0):
    """
    Compare latest close from Yahoo vs CNBC. Verdicts:
      AGREE      — within tol_pct; corroborated by two independent feeds.
      DIVERGE    — beyond tol; likely unadjusted split / bad print. Don't trade until resolved.
      ONE-SOURCE — only one feed responded; level rests on a single source.
      NO-DATA    — neither responded.
    """
    result = {"ticker": ticker, "tol_pct": tol_pct}
    yc = cc = None

    try:
        yb, _ = validate_bars(fetch_yahoo(ticker, "daily"), f"Yahoo ({ticker})")
        yc = yb[-1].c if yb else None
        result["yahoo_close"] = round(yc, 2) if yc else None
        result["yahoo_asof"] = yb[-1].date if yb else None
    except SystemExit as e:
        result["yahoo_error"] = str(e)

    try:
        cq = fetch_cnbc_quote(ticker)
        cc = cq["last"]
        result["cnbc_close"] = round(cc, 2)
        result["cnbc_asof"] = cq.get("asof")
    except SystemExit as e:
        result["cnbc_error"] = str(e)

    if yc is None and cc is None:
        result["verdict"] = "NO-DATA"
        return result
    if yc is None or cc is None:
        have = "Yahoo" if yc else "CNBC"
        result["verdict"] = f"ONE-SOURCE ({have} only)"
        result["close"] = round((yc or cc), 2)
        result["note"] = "second feed unavailable; level rests on a single source — cross-check manually"
        return result

    diff_pct = abs(yc - cc) / ((yc + cc) / 2) * 100 if (yc + cc) else 999
    result["diff_pct"] = round(diff_pct, 2)
    if diff_pct <= tol_pct:
        result["verdict"] = "AGREE"
    else:
        result["verdict"] = "DIVERGE"
        result["note"] = ("feeds disagree beyond tolerance — likely an unadjusted split, an "
                          "after-hours print, or a bad wick on one side; verify before trading the level")
    return result


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Cross-check latest close across Yahoo + CNBC (independent feeds).")
    ap.add_argument("--tickers", required=True, help="Comma-separated symbols.")
    ap.add_argument("--tol", type=float, default=1.0, help="Agreement tolerance in %% (default 1.0).")
    args = ap.parse_args()

    print(f"{'Ticker':<8}{'Yahoo':>10}{'CNBC':>10}{'Diff%':>8}  Verdict")
    print("-" * 60)
    for t in [x.strip() for x in args.tickers.split(",") if x.strip()]:
        r = cross_check(t, args.tol)
        yc = r.get("yahoo_close", "-")
        cc = r.get("cnbc_close", "-")
        dp = r.get("diff_pct", "-")
        print(f"{t:<8}{str(yc):>10}{str(cc):>10}{str(dp):>8}  {r['verdict']}")
        if r.get("note"):
            print(f"         > {r['note']}")
    print("\nAGREE = corroborated by two independent feeds. DIVERGE = verify before trading. "
          "Note: CNBC 'last' may be an after-hours print when markets are open, so a small "
          "intraday diff is normal. Not financial advice.")


if __name__ == "__main__":
    main()
