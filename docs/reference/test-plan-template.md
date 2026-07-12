# Test-plan template

Engagement: {{name}}
Asset under test: {{asset}}
Scope match: {{exact / excluded}}
Authorized test class: {{web / api / auth}}

## Hypothesis
{{what security boundary should hold}}

## Preconditions
- Role: {{}}
- Owned accounts: {{}}
- Synthetic data: {{}}

## Minimal experiment
1. Baseline: {{authorized action succeeds}}
2. Change only: {{variable}}
3. Observe: {{expected vs actual}}

## Controls
- Positive: {{}}
- Negative: {{}}
- Cross-account: {{}}
- Clean-session: {{}}

## Evidence
- Request/response IDs: {{}}
- Timestamps: {{}}

## Stop condition
{{trigger that halts test}}

## Result
- Reproduced: {{yes/no}}
- Confidence: {{lead/candidate/validated/reportable}}
- Risk score: {{0-15}}
