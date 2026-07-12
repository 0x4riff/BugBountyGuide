# Web testing

## Access control

Use two owned accounts. Test horizontal and vertical boundaries by changing one object reference or action. Confirm server-side result, not UI visibility.

## Injection

Prefer harmless canaries and timing controls. Encoding changes, error pages, or response-size differences alone do not prove injection. Require deterministic behavior and alternative explanation checks.

## Server-side request behavior

Use a domain you control only when policy permits callbacks. Distinguish browser fetches, redirects, link previews, and server-side requests. Never probe private networks or cloud metadata without explicit permission.

## Cache behavior

Establish cacheability first. Separate cache key, cache storage, and victim impact. Use harmless markers and your own sessions. Never poison shared production content.

## File handling

Test synthetic files. Verify storage, retrieval authorization, content-type handling, and transformation. Do not upload executable malware or polyglots unless explicitly allowed in a lab.
