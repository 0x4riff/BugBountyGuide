# Knowledge Base: SSRF

## CWE-918: Server-Side Request Forgery

### OWASP Category
A10:2021 — Server-Side Request Forgery

### Description
The web application fetches a remote resource without validating the user-supplied URL, allowing an attacker to coerce the application to send crafted requests to unexpected destinations.

### Common patterns
- Image URL parameter: `?url=https://evil.com/callback`
- Webhook configuration: `{"callback_url": "http://169.254.169.254/latest/meta-data/"}`
- PDF generation with external CSS/image
- XML External Entity (XXE) in document parsing
- Link preview / unfurl features

### Safe test methodology
1. Use a domain you control (e.g., Burp Collaborator, webhook.site)
2. Test with `http://YOUR-COLLABORATOR-ID.burpcollaborator.net`
3. Confirm server-side request (not browser redirect)
4. Test internal IP ranges only with explicit permission
5. NEVER probe cloud metadata (169.254.169.254) unless explicitly allowed

### Evidence to capture
- Request with your controlled URL
- DNS/HTTP callback logs showing server-side request
- Response indicating fetched content

### Safe payloads
```http
POST /api/webhook HTTP/1.1
Content-Type: application/json

{"url": "https://YOUR-COLLABORATOR.burpcollaborator.net"}
```

### Remediation
- Allowlist outbound destinations
- Block requests to internal/private IP ranges
- Disable unnecessary URL schemes (file://, gopher://)
- Use DNS resolution validation before connection

### CVSS v3.1 base
- Attack Vector: Network
- Attack Complexity: Low
- Privileges Required: Low
- User Interaction: None
- Scope: Unchanged
- Confidentiality: High
- Integrity: Low
- Availability: None
- **Score: 7.2 (High)** — AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N

### References
- https://cwe.mitre.org/data/definitions/918.html
- https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/
- https://portswigger.net/web-security/ssrf
