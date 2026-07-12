---
name: ai-bug-bounty-guide
description: "Authorized AI-assisted bug-bounty planning, scope validation, passive recon, safe testing, finding validation, and report drafting for web and API programs. Use when user asks to assess an explicitly authorized target or bug-bounty scope."
license: CC-BY-4.0
homepage: https://github.com/0x4riff/BugBountyGuide
---

# AI Bug Bounty Guide

Orchestrate authorized research. Never treat a hostname alone as permission.

## Mandatory gate

Before active testing, obtain and record:

- Program or authorization source
- Exact in-scope assets
- Allowed and prohibited test classes
- Automation/rate limits
- Researcher identification/header requirements
- Account/data restrictions

If authorization is absent or ambiguous, perform no active probing. Ask for program policy URL or written authorization. Passive public-information review may continue only without interacting with target infrastructure.

Run `scripts/scope_guard.py` against completed scope manifest. Continue only when it returns `AUTHORIZED`.

## Workflow

1. Create engagement folder from `assets/engagement-template.md`.
2. Fill `scope.json` using `references/scope-schema.md`.
3. Run scope guard.
4. Build attack-surface inventory from authorized sources.
5. Form test hypotheses using `references/agent-playbook.md`.
6. Start passive; use lowest-impact request capable of answering hypothesis.
7. Apply positive, negative, cross-account, and clean-session controls.
8. Store redacted evidence. Never store live secrets in Git.
9. Stop after reproducible minimum proof.
10. Draft report from `assets/report-template.md`.

## Agent roles

For multi-agent runtimes, split work by artifact, not uncontrolled target access:

- Scope agent: policy extraction and authorization matrix
- Recon agent: passive inventory and hypotheses
- Test planner: minimal safe test plans; no execution without gate
- Validator: alternative explanations and false-positive controls
- Reporter: concise report and remediation

One coordinator owns request budget and stop decision. Agents must not independently widen scope.

## Non-negotiable stops

Stop on real-user data, credentials, production instability, destructive state change, third-party assets, out-of-scope redirects, or unclear authorization. Do not perform denial of service, phishing, credential attacks, persistence, malware, stealth/evasion, secret harvesting, or private-network/cloud-metadata probing unless program explicitly authorizes exact action.

## References

Load only as needed:

- `references/agent-playbook.md`
- `references/scope-schema.md`
- `references/validation-gates.md`
- Existing `docs/` chapters for test-class guidance
