# Advanced operating model

## Engagement state machine

`DRAFT → AUTHORIZED → MAPPED → TESTING → VALIDATING → REPORTING → CLOSED`

Transitions require explicit artifacts. Any stop condition moves state to `PAUSED`; scope violation moves it to `BLOCKED`.

## Artifact contract

- Scope manifest: authority, assets, exclusions, technique restrictions, limits
- Inventory: asset, source, scope match, auth context, confidence
- Trust map: actors, objects, states, enforcement points, integrations
- Hypothesis ledger: claim, prerequisite, changed variable, controls, request cost
- Evidence index: redacted request/response IDs, timestamps, hashes
- Finding ledger: candidate, confidence, impact, validation status, duplicate risk
- Stop log: trigger, time, affected work, coordinator decision

## Risk budget

Score each planned test:

- Request volume: 0–3
- State mutation: 0–3
- Data sensitivity: 0–3
- Service stability: 0–3
- Third-party interaction: 0–3

High score requires stronger policy language and human review. Undefined score means no execution.

## Confidence model

- Lead: tool or observation only
- Candidate: reproducible anomaly
- Validated: controls eliminate common alternatives
- Reportable: concrete security boundary and impact proven safely

Never call lead a vulnerability.

## Quality metrics

Track confirmed-to-submitted ratio, duplicate rate, false-positive rate, average requests per validated finding, policy deviations, and evidence completeness. Do not optimize raw request count.
