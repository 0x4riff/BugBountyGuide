# Knowledge Base: API Security

## CWE-284: Improper Access Control
## CWE-306: Missing Authentication for Critical Function

### OWASP Category
A01:2021 — Broken Access Control / A05:2021 — Security Misconfiguration

### Common API patterns
- BOLA: `/api/v1/users/{id}/profile` — change ID
- Mass assignment: `{"role": "admin"}` in user update
- GraphQL introspection leaking schema
- Rate limit bypass via header manipulation
- IDOR in RESTful nested resources
- Verbose error messages leaking internal paths

### Safe test methodology
1. Map all API endpoints (Swagger, GraphQL introspection, traffic capture)
2. Test authentication on each endpoint (no auth, expired token, wrong user)
3. Test authorization with cross-account access
4. Check mass assignment by adding extra fields
5. Test rate limits with sustained requests

### Evidence to capture
- API endpoint discovered
- Unauthorized access proof
- Schema leakage from introspection

### Safe payloads
```http
# BOLA test
GET /api/v1/users/OTHER-USER-ID/profile HTTP/1.1
Authorization: Bearer <your-token>

# Mass assignment
PUT /api/v1/users/me HTTP/1.1
Content-Type: application/json
Authorization: Bearer <your-token>

{"name": "test", "role": "admin"}

# GraphQL introspection
POST /graphql HTTP/1.1
Content-Type: application/json

{"query": "{ __schema { types { name fields { name } } } }"}
```

### CVSS v3.1 base (BOLA)
- Score: 6.5 (Medium) — AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N

### References
- https://owasp.org/API-Security/
- https://cwe.mitre.org/data/definitions/284.html
- https://portswigger.net/web-security/graphql
