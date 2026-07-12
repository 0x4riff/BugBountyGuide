# Tooling and obsolete advice

Tools accelerate observation; they do not establish vulnerability.

## Keep current

- Pin tool versions for reproducibility.
- Read changelogs before copying flags from old one-liners.
- Prefer structured output (JSON) over fragile text pipelines.
- Use request budgets, deduplication, backoff, and audit logs.
- Validate templates before running scanners.

## Advice to retire

- Blindly chaining many recon tools against every discovered host
- Treating every internal hostname or banner as medium severity
- Publishing live tokens, target lists, or copied private data
- Using status code or response length as sole SQLi/IDOR proof
- Assuming `X-Frame-Options: SAMEORIGIN` means same site; it means same origin
- Claiming JWT `alg:none`, request smuggling, or cache poisoning from scanner output alone
- Testing cloud metadata, private IP ranges, or destructive races without explicit permission

Use OWASP Web Security Testing Guide, OWASP API Security Top 10, PortSwigger Web Security Academy, and program policy as maintained references.
