# Scope manifest schema

Create `scope.json` per engagement:

```json
{
  "program": "Program name",
  "authorization_url": "https://program.example/policy",
  "authorization_confirmed": true,
  "assets": ["app.example.com", "api.example.com"],
  "excluded_assets": ["status.example.com"],
  "allowed_tests": ["web", "api", "authorization-own-accounts"],
  "prohibited_tests": ["dos", "social-engineering", "credential-attacks"],
  "max_requests_per_second": 2,
  "required_header": "X-Researcher: handle",
  "accounts_owned": 2,
  "notes": "Use synthetic data only"
}
```

`authorization_confirmed` must represent real evidence, not agent assumption. Wildcards follow program wording. Redirects and third-party services do not inherit scope.
