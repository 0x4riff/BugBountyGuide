# Quickstart for OpenClaw

## 1. Install

Clone repository into OpenClaw skills directory or reference repository through your supported skill installation flow. `SKILL.md` is entry point.

## 2. Provide authorization evidence

Good request:

```text
Use AI Bug Bounty Guide for this program: <policy URL>.
Extract scope first. Do not send active traffic until scope manifest passes.
Use maximum 2 requests/second and only my two test accounts.
```

Insufficient request:

```text
Scan example.com for bugs.
```

Hostname alone does not prove permission.

## 3. Create engagement manifest

Copy `scope.example.json`, replace example values, and preserve policy wording. Validate:

```bash
uv run python scripts/scope_guard.py engagements/example/scope.json
```

Expected:

```text
AUTHORIZED: manifest passed structural safety gate; human must still follow current program policy
```

## 4. Run phase by phase

Ask agent to produce one artifact at a time:

1. Authorization matrix
2. Asset inventory
3. Trust-boundary map
4. Ranked hypothesis ledger
5. Minimal test plans
6. Validation records
7. Report draft

Do not use one giant “find everything” prompt. Phase isolation improves oversight, evidence quality, and recovery.

## 5. Multi-agent mode

Coordinator assigns artifacts. Only designated executor sends approved target traffic. Validator works from redacted evidence and attempts to disprove candidates. Reporter never upgrades severity beyond evidence.
