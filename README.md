# Northbay Fitness – Membership Revenue Report

Fictional fitness studio (all data is made up). This small Python tool reads the
active-membership export and reports, for the finance lead:

- active members by plan
- monthly recurring revenue (MRR)
- average revenue per member

Plans are billed **monthly** or **annually**. MRR must express every plan as a
monthly amount, so an annual price is divided by 12. Paused memberships are not
counted.

## Run it

```
pip install -r requirements.txt
python src/revenue_report.py data/memberships.csv
```

## Run the tests

```
pytest
```

## Known issue
Finance says MRR is far too high since annual plans were introduced.
