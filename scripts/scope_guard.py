#!/usr/bin/env python3
"""Validate authorization manifest before active bug-bounty work."""
import json, sys
from pathlib import Path

REQUIRED = ["program", "authorization_url", "authorization_confirmed", "assets", "allowed_tests", "prohibited_tests", "max_requests_per_second"]
PROHIBITED_BASELINE = {"dos", "social-engineering", "credential-attacks"}

def fail(msg):
    print(f"BLOCKED: {msg}")
    raise SystemExit(1)

def main():
    if len(sys.argv) != 2:
        fail("usage: scope_guard.py scope.json")
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        fail(f"invalid manifest: {exc}")
    missing = [k for k in REQUIRED if k not in data]
    if missing: fail("missing fields: " + ", ".join(missing))
    if data["authorization_confirmed"] is not True: fail("authorization not confirmed")
    if not str(data["authorization_url"]).startswith("https://"): fail("authorization_url must be HTTPS evidence")
    if not isinstance(data["assets"], list) or not data["assets"]: fail("assets must be non-empty list")
    if any(a in ("*", "*.*") for a in data["assets"]): fail("unbounded wildcard asset")
    if not isinstance(data["max_requests_per_second"], (int, float)) or not 0 < data["max_requests_per_second"] <= 10: fail("request rate must be >0 and <=10")
    prohibited = {str(x).lower() for x in data["prohibited_tests"]}
    missing_stops = PROHIBITED_BASELINE - prohibited
    if missing_stops: fail("baseline prohibitions missing: " + ", ".join(sorted(missing_stops)))
    print("AUTHORIZED: manifest passed structural safety gate; human must still follow current program policy")

if __name__ == "__main__": main()
