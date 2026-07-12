# API and GraphQL testing

## API authorization matrix

Create matrix of role × action × object ownership × state. Test documented and client-used endpoints before random enumeration.

## Mass assignment

Compare accepted fields against schema and server response using your own object. A reflected field is not impact; prove unauthorized state change safely.

## Version drift

Compare active API versions for missing authorization, validation, and deprecation controls. Both versions must be in scope.

## GraphQL

- Enumerate operations from official clients and schema where permitted.
- Check resolver-level authorization with owned accounts.
- Test aliases/batching only within rate-limit policy.
- Validate field-level exposure and mutation state transitions.
- Complexity or depth is reportable only with safe, measurable impact and permitted testing.

## Common false positives

HTTP 200 with `errors`, empty objects echoing supplied IDs, different response lengths, and verbose schema errors are not authorization bypasses by themselves.
