# Identity, OAuth, and sessions

## Session checks

Test rotation after login and privilege change, logout invalidation, concurrent session policy, cookie attributes, CSRF boundaries, and sensitive-action reauthentication.

## OAuth/OIDC

Validate exact redirect URI matching, `state` binding, PKCE enforcement for public clients, issuer/audience checks, nonce handling, code reuse, and account-linking logic.

Use only clients and accounts you own. Never capture another user's authorization code or token.

## False-positive controls

- CSRF token expiry is not authentication bypass.
- A JWT decoding successfully says nothing about signature validation.
- Missing cookie flag needs realistic exploit conditions and impact.
- Open redirect becomes security-relevant only when trust or data crosses boundary.
