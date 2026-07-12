#!/usr/bin/env python3
"""Auto-deploy — Sync engagement to cloud storage or GitHub issue tracker."""
import json, subprocess, sys
from pathlib import Path

def deploy_to_github(engagement_path: str, repo: str = None):
    eng = Path(engagement_path)
    scope = json.loads((eng / "scope.json").read_text(encoding="utf-8-sig"))
    findings = json.loads((eng / "findings.json").read_text(encoding="utf-8-sig"))
    program = scope.get("program", "unknown")
    title = f"Bug Bounty Engagement: {program}"
    body_lines = [f"## Program: {program}", "", "### Findings", ""]
    for f in findings:
        body_lines.append(f"- [{f.get('id')}] {f.get('title')} (Risk: {f.get('risk_score', 'N/A')}/15, Status: {f.get('status')})")
    body = "\n".join(body_lines)
    if repo:
        cmd = ["gh", "issue", "create", "--repo", repo, "--title", title, "--body", body]
        print(f"Creating issue in {repo}...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Issue created: {result.stdout.strip()}")
        else:
            print(f"Error: {result.stderr}")
    else:
        print("No repo specified; printing issue body:")
        print(body)

def main():
    if len(sys.argv) < 2:
        print("usage: python auto_deploy.py <engagement_path> [github_repo]")
        sys.exit(1)
    deploy_to_github(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)

if __name__ == "__main__": main()
