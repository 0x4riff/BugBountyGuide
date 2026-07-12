# AI bug bounty cheatsheet

## Before any traffic
- Policy URL captured and scope manifest completed
- `scope_guard.py` returns `AUTHORIZED`
- Two owned accounts and synthetic data ready
- Rate limit below program ceiling

## Hypothesis template
```yaml
id: HYP-001
boundary: Account B must not read Account A object
changed_variable: object_id only
positive_control: Account A reads own object
negative_control: nonexistent object -> not found
cross_account_control: Account B denied
stop_condition: real-user data appears
```

## False-positive red flags
- HTTP 500 without sensitive data
- Internal hostname without reachable service/secret
- CORS header without credentialed readable response
- Response-size difference alone
- CSRF token expiry interpreted as auth bypass
- JWT that decodes but signature unverified
- Scanner signature without manual reproduction

## Reporting one-liner
```text
Title: <class> on <asset> allows <impact>
Steps: 1..n (minimal)
Impact: <concrete capability>
Evidence: redacted request/response + timestamp
```

## Never
- DoS, phishing, credential attacks, persistence, malware, stealth
- Cloud metadata or private-network probing without explicit permission
- Treat hostname as authorization
- Report without clean-session reproduction
