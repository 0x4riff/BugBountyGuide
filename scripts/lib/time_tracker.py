#!/usr/bin/env python3
"""Time Tracker — Log time spent per engagement phase."""
import json, time, sys
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parent.parent / "engagements" / ".time-log.json"

def _load():
    if LOG_PATH.exists():
        return json.loads(LOG_PATH.read_text(encoding="utf-8"))
    return {"sessions": []}

def _save(data):
    LOG_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

def start(engagement: str, phase: str):
    data = _load()
    entry = {
        "engagement": engagement,
        "phase": phase,
        "start": time.time(),
        "end": None,
        "duration_sec": 0
    }
    data["sessions"].append(entry)
    _save(data)
    print(f"timer started: {engagement}/{phase}")

def stop(engagement: str):
    data = _load()
    for s in reversed(data["sessions"]):
        if s["engagement"] == engagement and s["end"] is None:
            s["end"] = time.time()
            s["duration_sec"] = round(s["end"] - s["start"], 2)
            _save(data)
            print(f"timer stopped: {s['phase']} ({s['duration_sec']}s)")
            return
    print("no active session found")

def summary(engagement: str):
    data = _load()
    totals = {}
    for s in data["sessions"]:
        if s["engagement"] == engagement and s["end"] is not None:
            totals[s["phase"]] = totals.get(s["phase"], 0) + s["duration_sec"]
    print(f"Time summary for {engagement}:")
    for phase, secs in totals.items():
        print(f"  {phase}: {secs/3600:.1f}h")

def main():
    if len(sys.argv) < 3:
        print("usage: python time_tracker.py <engagement> start|stop|summary [phase]")
        sys.exit(1)
    engagement = sys.argv[1]
    action = sys.argv[2]
    phase = sys.argv[3] if len(sys.argv) > 3 else "general"
    if action == "start": start(engagement, phase)
    elif action == "stop": stop(engagement)
    elif action == "summary": summary(engagement)
    else: print("unknown action")

if __name__ == "__main__": main()
