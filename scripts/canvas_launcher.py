#!/usr/bin/env python3
"""Open the interactive Canvas Control Center on connected nodes."""
import json, sys, shutil
from pathlib import Path

def main():
    # Resolve paths
    workspace_root = Path(__file__).parent.parent.resolve()
    dashboard_src = workspace_root / "assets" / "canvas" / "dashboard.html"

    # Check default OpenClaw canvas path or prompt user
    target_canvas_dir = Path.home() / ".openclaw" / "canvas"

    if not target_canvas_dir.exists():
        target_canvas_dir.mkdir(parents=True, exist_ok=True)

    dashboard_dest = target_canvas_dir / "bug_bounty_guide_dashboard.html"
    shutil.copy2(dashboard_src, dashboard_dest)

    print("UI COPY: PASS")
    print(f"Canvas dashboard copied to: {dashboard_dest}")
    print("\nTo load this dashboard in OpenClaw, run the following tool command:")
    print("canvas(action='present', url='/__openclaw__/canvas/bug_bounty_guide_dashboard.html')")

if __name__ == "__main__":
    main()
