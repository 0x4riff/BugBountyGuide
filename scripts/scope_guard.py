#!/usr/bin/env python3
"""Validate authorization manifest against JSON schema and rules."""
import json, sys
from pathlib import Path

REQUIRED = ["program", "authorization_url", "authorization_confirmed", "assets", "allowed_tests", "prohibited_tests", "max_requests_per_second", "accounts_owned"]
PROHIBITED_BASELINE = {"dos", "social-engineering", "credential-attacks"}

def fail(msg):
    print(f"BLOCKED: {msg}", file=sys.stderr)
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        fail("usage: scope_guard.py scope.json")

    path = Path(sys.argv[1])
    if not path.is_file():
        fail(f"manifest file not found: {path}")

    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        fail(f"invalid JSON structure: {exc}")

    # 1. Structural validation
    missing = [k for k in REQUIRED if k not in data]
    if missing:
        fail("missing required fields: " + ", ".join(missing))

    # 2. Authorization check
    if data["authorization_confirmed"] is not True:
        fail("authorization_confirmed must be set to true")
    if not str(data["authorization_url"]).startswith("https://"):
        fail("authorization_url must provide secure HTTPS evidence")

    # 3. Asset verification
    if not isinstance(data["assets"], list) or not data["assets"]:
        fail("assets must be a non-empty array")

    for asset in data["assets"]:
        if asset.startswith("*."):
            fail(f"unresolved wildcard asset: {asset}. Wildcards must be resolved to concrete target hostnames.")
        if asset in ("*", "*.*"):
            fail("unbounded wildcard asset is prohibited")

    # 4. Limits verification
    rate = data["max_requests_per_second"]
    if not isinstance(rate, (int, float)) or not 0.1 <= rate <= 10.0:
        fail(f"max_requests_per_second ({rate}) out of limits [0.1, 10.0]")

    # 5. Accounts safety check
    accounts = data["accounts_owned"]
    if not isinstance(accounts, int) or accounts < 2:
        fail(f"accounts_owned ({accounts}) must be an integer >= 2 for authorization testing")

    # 6. Prohibited test verification
    prohibited = {str(x).lower() for x in data["prohibited_tests"]}
    missing_stops = PROHIBITED_BASELINE - prohibited
    if missing_stops:
        fail("baseline safety prohibitions missing: " + ", ".join(sorted(missing_stops)))

    # Optional JSON Schema verification
    schema_path = Path(__file__).parent.parent / "schemas" / "scope-schema.json"
    if schema_path.is_file():
        try:
            import jsonschema
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            jsonschema.validate(instance=data, schema=schema)
            print("Schema validation: PASS")
        except ImportError:
            print("Warning: jsonschema package not installed. Skipping schema validation.")
        except Exception as exc:
            fail(f"JSON Schema validation failed: {exc}")

    print("AUTHORIZED: manifest passed structural safety gate; human must still follow current program policy")

if __name__ == "__main__":
    main()
