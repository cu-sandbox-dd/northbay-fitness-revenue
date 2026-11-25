import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from revenue_report import load_members, mrr, members_by_plan, arpm  # noqa: E402

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "memberships.csv")


def test_members_by_plan_ignores_paused():
    assert members_by_plan(load_members(DATA)) == {"Basic": 3, "Premium": 3, "Studio Plus": 1}


def test_mrr_converts_annual_plans_to_monthly():
    assert mrr(load_members(DATA)) == 399.0


def test_arpm():
    assert arpm(load_members(DATA)) == 57.0
