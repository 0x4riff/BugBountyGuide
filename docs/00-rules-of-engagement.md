# Rules of engagement

## Before testing

1. Confirm exact asset is in scope, including hostname, mobile app, API, and environment.
2. Record forbidden classes: denial of service, social engineering, physical testing, rate-limit testing, automated scanning, or data access.
3. Identify account and identity restrictions.
4. Configure conservative request rate below published limit.
5. Add required researcher header when program requests one.
6. Prepare synthetic records and two accounts you control.

## Stop conditions

Stop and report when you encounter real user data, credentials, internal secrets, production instability, irreversible state changes, or evidence exceeding minimum needed.

Never use persistence, stealth, phishing, malware, credential stuffing, destructive payloads, or third-party infrastructure without authorization.
