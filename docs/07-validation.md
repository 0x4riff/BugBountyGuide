# Validation and false positives

Before reporting, answer:

1. What security boundary should hold?
2. What exact request breaks it?
3. Can you reproduce from clean state?
4. What negative control behaves correctly?
5. Is behavior documented or used by official clients?
6. Is data/action outside your authorized account?
7. What realistic attacker prerequisite exists?
8. What minimum evidence proves impact?

## Frequent traps

- HTTP 500 or stack trace without sensitive data
- Internal hostname without reachable service or secret
- CORS header without credentialed readable response
- Missing rate limit when policy excludes it
- Scanner signature without manual reproduction
- Boolean SQL injection based only on unstable response size
- “Premium bypass” caused by public endpoint or normal token flow
- Self-XSS without credible victim interaction boundary
