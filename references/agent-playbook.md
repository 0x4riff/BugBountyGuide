# AI agent playbook

## Coordinator contract

Maintain scope manifest, request budget, evidence index, findings ledger, and stop log. Reject tasks lacking asset-to-scope match.

## Phase outputs

### Scope

Output authorization summary, asset patterns, exclusions, limits, and unresolved questions. No target traffic.

### Recon

Output deduplicated inventory with source and confidence. Active discovery requires authorization gate. Never infer scope from DNS adjacency or company ownership.

### Hypothesis

Each item states boundary, prerequisite, one changed variable, expected result, safe test, controls, stop condition, and evidence needed.

### Validation

Try to disprove finding. Check intended behavior, official client flow, caching, stale session, normalization, race noise, and scanner signature quality.

### Reporting

Include exact asset, prerequisites, minimal steps, expected/actual, concrete impact, redacted evidence, and remediation. Separate observed facts from inference.

## Useful prompts

- “Extract scope and restrictions from this program policy. Do not test anything.”
- “Create safe hypotheses for these authorized endpoints, ranked by signal and impact.”
- “Challenge this candidate finding using negative controls and alternative explanations.”
- “Turn this redacted evidence into concise report without inflating severity.”
