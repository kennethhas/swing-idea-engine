#!/usr/bin/env python3
"""Regression tests for the swing gate engine. Stdlib only - no pytest needed.

Run:  python3 tests/test_gates.py
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from gates import evaluate  # noqa: E402


def base(**kw):
    """A clean CRM-shaped long that passes every gate."""
    d = {"direction": "long", "price": 234.69, "proximal": 209.17, "distal": 198.95,
         "stop": 197.93, "target": 253.62, "target_tf": "weekly", "odds": 8,
         "tested": 1, "bars_ltf": 180, "earnings_days": 42, "pass2": False}
    d.update(kw)
    return d


def g(gates, name):
    return next(x for x in gates if x["gate"] == name)["status"]


class TestVerdicts(unittest.TestCase):

    def test_clean_long_trades_with_expected_rr(self):
        v, gates, m = evaluate(base())
        self.assertEqual(v, "TRADE")
        self.assertAlmostEqual(m["rr"], 3.954, places=2)   # the real CRM number

    def test_rr_below_three_is_ineligible(self):
        # target pulled in so R:R lands just under 3:1
        v, gates, _ = evaluate(base(target=240.00))
        self.assertEqual(v, "INELIGIBLE")
        self.assertEqual(g(gates, "R:R"), "FAIL")

    def test_rr_exactly_three_passes(self):
        # risk 11.24 -> reward 33.72 -> target 242.89
        v, gates, m = evaluate(base(target=209.17 + 3 * 11.24))
        self.assertEqual(g(gates, "R:R"), "PASS")
        self.assertAlmostEqual(m["rr"], 3.0, places=6)
        self.assertEqual(v, "TRADE")

    def test_missing_target_is_ineligible_even_though_rr_absent(self):
        v, gates, _ = evaluate(base(target=None))
        self.assertEqual(v, "INELIGIBLE")
        self.assertEqual(g(gates, "Target"), "FAIL")

    def test_price_inside_zone_caps_at_watch_not_trade(self):
        # price sits between distal and proximal -> reacting, never a clean entry
        v, gates, _ = evaluate(base(price=205.00, target=253.62))
        self.assertEqual(v, "WATCH")
        self.assertEqual(g(gates, "Price-inside-zone"), "FAIL")

    def test_pass2_zone_caps_at_watch(self):
        v, gates, _ = evaluate(base(pass2=True))
        self.assertEqual(v, "WATCH")

    def test_tested_twice_is_ineligible(self):
        v, gates, _ = evaluate(base(tested=2))
        self.assertEqual(v, "INELIGIBLE")
        self.assertEqual(g(gates, "Freshness"), "FAIL")

    def test_odds_below_six_is_ineligible(self):
        v, gates, _ = evaluate(base(odds=5))
        self.assertEqual(v, "INELIGIBLE")
        self.assertEqual(g(gates, "Odds score"), "FAIL")

    def test_earnings_inside_buffer_blocks(self):
        v, gates, _ = evaluate(base(earnings_days=3))
        self.assertEqual(v, "INELIGIBLE")

    def test_unverified_earnings_blocks_rather_than_assuming_clear(self):
        v, gates, _ = evaluate(base(earnings_days=None))
        self.assertEqual(v, "INELIGIBLE")
        self.assertIn("NOT VERIFIED", g_detail(gates, "Earnings"))

    def test_too_few_ltf_bars_is_ineligible(self):
        v, gates, _ = evaluate(base(bars_ltf=59))
        self.assertEqual(v, "INELIGIBLE")
        self.assertEqual(g(gates, "Bars"), "FAIL")

    def test_artifact_rr_is_flagged_not_silently_sold(self):
        v, gates, m = evaluate(base(target=209.17 + 20 * 11.24))
        self.assertTrue(any("ARTIFACT" in f for f in m["flags"]))

    def test_demand_zone_above_price_fails_side_of_price(self):
        v, gates, _ = evaluate(base(price=150.00))
        self.assertEqual(g(gates, "Side of price"), "FAIL")
        self.assertEqual(v, "INELIGIBLE")


class TestShorts(unittest.TestCase):

    def short(self, **kw):
        d = {"direction": "short", "price": 100.0, "proximal": 110.0, "distal": 115.0,
             "stop": 116.0, "target": 80.0, "target_tf": "daily", "odds": 7,
             "tested": 0, "bars_ltf": 120, "earnings_days": 30, "pass2": False}
        d.update(kw)
        return d

    def test_clean_short_trades(self):
        v, gates, m = evaluate(self.short())
        self.assertEqual(v, "TRADE")
        self.assertAlmostEqual(m["rr"], 5.0, places=6)   # (110-80)/(116-110)

    def test_short_always_carries_executability_flag(self):
        _, _, m = evaluate(self.short())
        self.assertTrue(any("EXECUTABILITY" in f for f in m["flags"]))

    def test_short_earnings_gate_applies_equally(self):
        v, _, _ = evaluate(self.short(earnings_days=2))
        self.assertEqual(v, "INELIGIBLE")

    def test_supply_zone_below_price_fails_side_of_price(self):
        v, gates, _ = evaluate(self.short(price=130.0))
        self.assertEqual(g(gates, "Side of price"), "FAIL")


def g_detail(gates, name):
    return next(x for x in gates if x["gate"] == name)["detail"]


if __name__ == "__main__":
    unittest.main(verbosity=2)
