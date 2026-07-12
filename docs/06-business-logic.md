# Business logic and race conditions

Model invariants: one-time use, balance conservation, quantity limits, approval order, role separation, and state prerequisites.

## Safe race testing

Use own account, lowest-value synthetic transaction, small bounded concurrency, and explicit policy permission. Confirm final server state and clean up. Stop on instability.

## High-signal areas

- Coupon, credit, refund, and invite reuse
- Multi-step workflow skipping
- Price/quantity trust boundaries
- Approval and account-linking races
- Idempotency-key scope and replay
- Cross-channel state mismatch between web, mobile, and API

A transient error or duplicate response is not proof. Demonstrate invariant violation in final state.
