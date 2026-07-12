# Reporting

## Recommended structure

- Title: vulnerability + asset + impact
- Summary: boundary broken in two sentences
- Preconditions: role, account, feature state
- Steps: numbered, minimal, reproducible
- Expected vs actual behavior
- Impact: concrete attacker capability
- Evidence: redacted requests/responses, timestamps, video only when useful
- Remediation: enforcement point and regression test idea

## Quality rules

Avoid inflated severity, unsupported CVSS, long recon narratives, duplicate screenshots, and claims such as “full compromise” without proof. Redact cookies, tokens, personal data, and internal identifiers not needed by triage.
