# Knowledge Base: Business Logic

## CWE-840: Business Logic Error

### OWASP Category
A04:2021 — Insecure Design

### Description
The application does not enforce constraints on the sequence of operations, allowing attackers to bypass business rules by manipulating the flow.

### Common patterns
- Negative quantity in order: `{"qty": -1}` → credit instead of debit
- Skip payment step: manipulate checkout flow to skip payment
- Price override: modify price field in client-side request
- Race condition: concurrent requests to redeem same coupon twice
- Workflow bypass: jump from step 1 to step 3 without completing step 2

### Safe test methodology
1. Map the intended workflow (happy path)
2. Identify state transitions and constraints
3. Test each constraint by sending out-of-sequence requests
4. Test boundary values: 0, -1, MAX_INT, empty, null
5. Use two concurrent requests for race condition tests

### Evidence to capture
- Request with manipulated business logic parameter
- Response showing unintended business outcome
- Before/after state comparison

### Safe payloads
```http
# Negative quantity
POST /api/cart/add HTTP/1.1
Content-Type: application/json

{"product_id": "SKU-001", "quantity": -1}

# Skip step
POST /api/checkout/complete HTTP/1.1
Content-Type: application/json

{"order_id": "ORD-1001", "step": 3}
```

### Remediation
- Validate business rules server-side on every transaction
- Implement idempotency keys for critical operations
- Use state machines for multi-step workflows
- Rate limit critical endpoints

### CVSS v3.1 base
- Attack Vector: Network
- Attack Complexity: Low
- Privileges Required: Low
- User Interaction: None
- Scope: Unchanged
- Confidentiality: Low
- Integrity: High
- Availability: None
- **Score: 5.4 (Medium)** — AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:H/A:N

### References
- https://cwe.mitre.org/data/definitions/840.html
- https://owasp.org/Top10/A04_2021-Insecure_Design/
- https://portswigger.net/web-security/logic-flaws
