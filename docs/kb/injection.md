# Knowledge Base: Injection

## CWE-79: Cross-Site Scripting (XSS)
## CWE-89: SQL Injection
## CWE-78: OS Command Injection

### OWASP Category
A03:2021 — Injection

### Description
Application sends untrusted data to an interpreter as part of a command or query, causing unintended execution.

### Common patterns
- Reflected input in HTML context: `?name=<script>alert(1)</script>`
- Stored user content rendered without encoding
- Search parameters in SQL queries: `?q=test%27+OR+1%3D1--`
- File upload with executable content-type
- Template injection in server-side rendering

### Safe test methodology
1. Use harmless canaries: `<canary>` not `<script>alert(1)</script>`
2. Prefer timing-based detection over exploitation
3. Test encoding variants (URL, HTML entity, Unicode)
4. Verify deterministic behavior (not one-off)
5. Check alternative explanations (error pages, caching)

### Evidence to capture
- Input with canary marker
- Response reflecting canary in executable context
- Proof of execution (DOM, network request, timing delay)

### Safe payloads
```http
# XSS canary (harmless)
GET /search?q=<canary-xss-test> HTTP/1.1

# SQLi timing test
GET /api/items?category=electronics%27+AND+SLEEP(5)-- HTTP/1.1

# Template injection canary
POST /api/render HTTP/1.1
Content-Type: application/json

{"template": "{{7*7}}"}
```

### Remediation
- Parameterized queries for all database access
- Output encoding appropriate to context (HTML, JS, URL, CSS)
- Content Security Policy headers
- Input validation with allowlists

### CVSS v3.1 base (Stored XSS)
- Attack Vector: Network
- Attack Complexity: Low
- Privileges Required: Low
- User Interaction: Required
- Scope: Changed
- Confidentiality: Low
- Integrity: Low
- Availability: None
- **Score: 6.1 (Medium)** — AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N

### References
- https://cwe.mitre.org/data/definitions/79.html
- https://cwe.mitre.org/data/definitions/89.html
- https://owasp.org/Top10/A03_2021-Injection/
- https://portswigger.net/web-security
