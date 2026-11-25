"""Membership revenue summary for Northbay Fitness (fictional)."""
import csv
import sys
from collections import Counter


def load_members(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["price"] = float(r["price"])
    return rows


def active_members(members):
    return [m for m in members if m["status"] == "active"]


def monthly_value(member):
    """What one membership is worth per month."""
    return member["price"]


def mrr(members):
    """Monthly recurring revenue from active members."""
    return round(sum(monthly_value(m) for m in active_members(members)), 2)


def members_by_plan(members):
    return dict(Counter(m["plan"] for m in active_members(members)))


def arpm(members):
    """Average monthly revenue per active member."""
    active = active_members(members)
    if not active:
        return 0.0
    return round(mrr(members) / len(active), 2)


def main(path):
    members = load_members(path)
    print("Active members by plan:", members_by_plan(members))
    print(f"MRR:  ${mrr(members):,.2f}")
    print(f"ARPM: ${arpm(members):,.2f}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/memberships.csv")
