# Methodology

## 1. Map trust boundaries

List actors, roles, objects, state transitions, integrations, and enforcement points. Focus on where client-controlled input crosses authorization or business rules.

## 2. Form a falsifiable hypothesis

Bad: “Endpoint looks vulnerable.”

Good: “Account B can read Account A invoice by replacing only `invoice_id`, although policy requires ownership.”

## 3. Run minimal experiment

Change one variable. Preserve baseline request. Avoid broad fuzzing until policy permits it and manual mapping shows value.

## 4. Add controls

- Positive control: own authorized object succeeds.
- Negative control: nonexistent object fails.
- Cross-account control: second owned account is denied.
- Clean-session control: repeat without stale cookies/cache.

## 5. Reproduce and stop

Reproduce twice when safe, document prerequisites, then stop. More records rarely increase impact.
