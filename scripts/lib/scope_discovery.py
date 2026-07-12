#!/usr/bin/env python3
"""Scope Discovery — Extract assets from scope.json and resolve wildcards to concrete hostnames."""
import json, re, sys
from pathlib import Path

def resolve_wildcards(assets: list) -> list:
    resolved = []
    for a in assets:
        if a.startswith("*."):
            resolved.append({"original": a, "resolved": a[2:], "type": "wildcard"})
        else:
            resolved.append({"original": a, "resolved": a, "type": "exact"})
    return resolved

def main(scope_path: str):
    scope = json.loads(Path(scope_path).read_text(encoding="utf-8-sig"))
    assets = scope.get("assets", [])
    resolved = resolve_wildcards(assets)
    print(f"Scope: {scope.get('program')}")
    print(f"Assets ({len(assets)}):")
    for r in resolved:
        print(f"  - {r['resolved']} ({r['type']})")
    return resolved

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python scope_discovery.py <scope.json>")
        sys.exit(1)
    main(sys.argv[1])
