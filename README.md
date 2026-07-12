# Bug Bounty Guide

[![License: CC BY 4.0](https://img.shields.io/badge/Content-CC_BY_4.0-blue.svg)](LICENSE)
[![Ethical Research](https://img.shields.io/badge/research-authorized_only-success.svg)](SECURITY.md)

Practical, scope-first field guide for finding and reporting web/API vulnerabilities with reproducible evidence and low false-positive rates.

> Test only assets and actions explicitly authorized by program policy. Stop when evidence is sufficient. Never access, alter, or retain other users' data.

## Why this guide

Many tip collections optimize for payload volume. This guide optimizes for **signal, validation, and report quality**.

- Modern web, API, GraphQL, OAuth/OIDC, cache, race-condition, and business-logic coverage
- False-positive controls beside each testing phase
- Safe proof patterns using own accounts and synthetic data
- Beginner-friendly workflow with decision gates
- No target lists, stolen secrets, destructive payloads, or scanner spam

## Start here

1. [Rules of engagement](docs/00-rules-of-engagement.md)
2. [Methodology](docs/01-methodology.md)
3. [Recon and attack-surface mapping](docs/02-recon.md)
4. [Web testing](docs/03-web-testing.md)
5. [API and GraphQL testing](docs/04-api-graphql.md)
6. [Identity, OAuth, and sessions](docs/05-identity.md)
7. [Business logic and race conditions](docs/06-business-logic.md)
8. [Validation and false positives](docs/07-validation.md)
9. [Reporting](docs/08-reporting.md)
10. [Tooling and obsolete advice](docs/09-tooling.md)

## Core loop

```text
Policy → Map → Hypothesis → Minimal test → Control test → Reproduce → Report → Stop
```

## High-signal habits

- Read policy before traffic generation; record prohibited test classes and rate limits.
- Use two accounts you own when testing authorization boundaries.
- Compare one variable at a time: identity, role, object ID, method, content type, or state.
- Capture raw request/response plus timestamp, account role, and expected behavior.
- Treat status-code differences as clues, not proof.
- Prove impact with minimum data necessary; redact tokens and personal data.
- Search public client code and official docs before labeling intended behavior a bypass.
- Re-test from clean session and include negative control.
- Prefer manual confirmation after automation; scanners produce leads, not findings.
- Stop immediately if test touches real user data or service stability.

## Quick checklists

- [Pre-test authorization](checklists/pre-test.md)
- [Finding validation](checklists/validation.md)
- [Report readiness](checklists/report-ready.md)

## Contributing

Corrections and safe techniques welcome. Every contribution needs source/rationale, validation controls, and clear authorization boundaries. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Attribution

Original work maintained by [0x4riff](https://github.com/0x4riff). Inspired by public bug-bounty community knowledge, OWASP testing guides, PortSwigger Web Security Academy, and disclosed reports. This repository does not copy the unlicensed contents of `KingOfBugBountyTips`.

## Disclaimer

Educational use and authorized security research only. You are responsible for complying with law, contracts, and program rules.
