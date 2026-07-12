#!/usr/bin/env python3
"""Test Runner — Execute hypothesis tests with rate limiting and stop conditions."""
import json, time, sys
from pathlib import Path

def run_test(test_file: str, rate_limit: float = 1.0):
    test = json.loads(Path(test_file).read_text(encoding="utf-8-sig"))
    print(f"Running: {test.get('id', 'unknown')}")
    print(f"Hypothesis: {test.get('boundary', 'N/A')}")
    results = {
        "test_id": test.get("id"),
        "status": "pending",
        "steps_run": 0,
        "controls_passed": 0,
        "controls_failed": 0,
        "stop_triggered": False,
        "stop_reason": None,
        "start_time": time.time(),
        "end_time": None,
        "duration_sec": 0
    }
    steps = test.get("steps", [])
    controls = test.get("controls", {})
    stop_conditions = test.get("stop_conditions", [])
    for i, step in enumerate(steps):
        print(f"  Step {i+1}: {step}")
        time.sleep(1.0 / rate_limit)
        results["steps_run"] += 1
    for name, expected in controls.items():
        print(f"  Control: {name} -> {expected}")
        results["controls_passed" if expected else "controls_failed"] += 1
    for cond in stop_conditions:
        if cond.get("triggered"):
            results["stop_triggered"] = True
            results["stop_reason"] = cond.get("reason")
            print(f"  STOP: {cond.get('reason')}")
            break
    results["end_time"] = time.time()
    results["duration_sec"] = round(results["end_time"] - results["start_time"], 2)
    results["status"] = "completed" if not results["stop_triggered"] else "stopped"
    print(f"Result: {results['status']} ({results['duration_sec']}s)")
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python test_runner.py <test.json> [rate_limit]")
        sys.exit(1)
    rl = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    run_test(sys.argv[1], rl)
