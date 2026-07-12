#!/usr/bin/env python3
"""Bug Bounty Guide CLI helper.

Subcommands:
  init      scaffold engagements/<name>/ with scope.json + findings.json
  validate  run scope_guard on engagements/<name>/scope.json
  score     compute risk_score (0-15) for a finding JSON
  report    render markdown report from engagements/<name>/findings.json
"""
import json, sys, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOPE_GUARD = ROOT / "scripts" / "scope_guard.py"
ENG = ROOT / "engagements"

def _load(p):
    return json.loads(Path(p).read_text(encoding="utf-8-sig"))

def init(name):
    d = ENG / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "scope.json").write_text(json.dumps({
        "program": name,
        "authorization_url": "",
        "authorization_confirmed": False,
        "assets": [],
        "excluded_assets": [],
        "allowed_tests": [],
        "prohibited_tests": ["dos", "social-engineering", "credential-attacks"],
        "max_requests_per_second": 1,
        "required_header": "",
        "accounts_owned": 2
    }, indent=2) + "\n", encoding="utf-8")
    (d / "findings.json").write_text("[]\n", encoding="utf-8")
    print(f"engagement scaffolded: {d}")

def validate(name):
    sp = ENG / name / "scope.json"
    return subprocess.run([sys.executable, str(SCOPE_GUARD), str(sp)]).returncode

def score(finding_path):
    f = _load(finding_path)
    m = f.get("methodology", {})
    def pts(v): return 3 if v in ("high","critical") else 2 if v in ("medium",) else 1 if v in ("low",) else 0
    score = pts(m.get("request_volume")) + pts(m.get("state_mutation")) + pts(m.get("data_sensitivity")) + pts(m.get("service_stability")) + pts(m.get("third_party"))
    f["risk_score"] = score
    Path(finding_path).write_text(json.dumps(f, indent=2) + "\n", encoding="utf-8")
    print(f"risk_score={score}/15 -> {finding_path}")
    return 0

def report(name):
    fs = _load(ENG / name / "findings.json")
    out = [f"# Findings — {name}\n"]
    for f in fs:
        out.append(f"## {f.get('id')} {f.get('title','')}\n")
        out.append(f"- Asset: {f.get('asset')}")
        out.append(f"- Class: {f.get('class')}")
        out.append(f"- Confidence: {f.get('confidence')}")
        out.append(f"- Risk: {f.get('risk_score')}/15")
        out.append(f"- Status: {f.get('status')}\n")
        out.append(f"**Impact:** {f.get('impact')}\n")
        out.append("**Steps:**")
        for s in f.get("steps", []): out.append(f"1. {s}")
        out.append(f"\n**Remediation:** {f.get('remediation')}\n")
    Path(ENG / name / "REPORT.md").write_text("\n".join(out), encoding="utf-8")
    print(f"report written: {ENG / name / 'REPORT.md'}")

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "init": init(sys.argv[2] if len(sys.argv)>2 else "default")
    elif cmd == "validate": sys.exit(validate(sys.argv[2] if len(sys.argv)>2 else "default"))
    elif cmd == "score":
        sys.exit(score(sys.argv[2]))
    elif cmd == "report": report(sys.argv[2] if len(sys.argv)>2 else "default")
    else:
        print("unknown command"); sys.exit(1)

if __name__ == "__main__": main()
