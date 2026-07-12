# AI-assisted hypothesis ledger

Use one record per hypothesis.

```yaml
id: HYP-001
asset: api.example.com
scope_match: exact
boundary: Account B must not read Account A object
prerequisites: two owned accounts
changed_variable: object_id only
baseline: Account A reads own synthetic object
negative_control: nonexistent object returns not found
cross_account_control: Account B must be denied
request_budget: 4
state_mutation: none
stop_condition: any real-user data appears
evidence_needed: redacted request and response pair
status: planned
confidence: lead
```

## Prioritization

Rank by authorization clarity, business boundary strength, safe reproducibility, expected impact, request cost, and duplicate likelihood. Prefer high-signal state and authorization logic over indiscriminate payload coverage.
