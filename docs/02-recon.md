# Recon and attack-surface mapping

## Passive first

Use program asset lists, certificate transparency, DNS, official apps, public documentation, JavaScript source maps when intentionally exposed, and archived URLs where policy allows.

## Build inventory

Track host, environment, owner, technology clue, authentication requirement, data class, and confidence. Deduplicate before probing.

## Modern tips

- Extract API schemas from OpenAPI, GraphQL introspection when enabled, and client bundles.
- Compare production and staging only when both are explicitly in scope.
- Map hidden workflow states, not only endpoints.
- Record mobile/web API version drift.
- Treat internal names and headers as informational until chained to concrete impact.

## Controls

A DNS record is not proof of ownership or scope. A live host is not permission to scan. Confirm scope before active requests.
