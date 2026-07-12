# Knowledge Base: IDOR & Access Control

## CWE-639: Authorization Bypass Through User-Controlled Key

### OWASP Category
A01:2021 — Broken Access Control

### Description
The system does not properly enforce authorization checks when a user accesses resources by modifying the key value (ID, filename, token) that identifies that resource.

### Common patterns
- Sequential IDs: `/api/invoice/1001` → change to `/api/invoice/1002`
- UUID in body but no ownership check: `{"invoice_id": "550e8400-e29b-41d4-a716-446655440000"}`
- File path traversal: `/files/report-2024.pdf` → `/files/report-2025.pdf`
- User ID in JWT claim but not checked server-side

### Safe test methodology
1. Create two owned accounts (A and B)
2. Account A creates synthetic resource with known ID
3. Account B requests Account A's resource ID
4. Verify server returns 403/404, not Account A's data
5. Test horizontal (same role) and vertical (admin vs user)

### Evidence to capture
- Request with Account B's auth + Account A's resource ID
- Response showing Account A's data (if vulnerable)
- Server-side confirmation (not just UI rendering)

### Safe payloads
```http
GET /api/invoice/INV-1001 HTTP/1.1
Authorization: Bearer <account-B-token>
```

### Remediation
- Implement ownership checks on every resource access
- Use indirect references (session-scoped mapping)
- Log unauthorized access attempts

### CVSS v3.1 base
- Attack Vector: Network
- Attack Complexity: Low
- Privileges Required: Low
- User Interaction: None
- Scope: Unchanged
- Confidentiality: High
- Integrity: None
- Availability: None
- **Score: 6.5 (Medium)** — AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N

### References
- https://cwe.mitre.org/data/definitions/639.html
- https://owasp.org/Top10/A01_2021-Broken_Access_Control/
- https://portswigger.net/web-security/access-control
