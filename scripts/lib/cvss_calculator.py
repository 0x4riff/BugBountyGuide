#!/usr/bin/env python3
"""CVSS v3.1 Calculator — compute severity from vector components."""
import sys

WEIGHTS = {
    "AV": {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2},
    "AC": {"L": 0.77, "H": 0.44},
    "PR": {"N": 0.85, "L": 0.62, "H": 0.27},
    "UI": {"N": 0.85, "R": 0.62},
    "S": {"U": 0, "C": 1},
    "C": {"N": 0, "L": 0.22, "H": 0.56},
    "I": {"N": 0, "L": 0.22, "H": 0.56},
    "A": {"N": 0, "L": 0.22, "H": 0.56}
}

def parse_vector(v: str) -> dict:
    parts = v.split("/")
    result = {}
    for part in parts:
        if ":" in part:
            k, val = part.split(":", 1)
            result[k] = val
    return result

def compute_cvss(vector: dict) -> float:
    av = WEIGHTS["AV"].get(vector.get("AV", "N"), 0.85)
    ac = WEIGHTS["AC"].get(vector.get("AC", "L"), 0.77)
    pr_base = WEIGHTS["PR"].get(vector.get("PR", "N"), 0.85)
    ui = WEIGHTS["UI"].get(vector.get("UI", "N"), 0.85)
    scope = vector.get("S", "U")
    c = WEIGHTS["C"].get(vector.get("C", "N"), 0)
    i = WEIGHTS["I"].get(vector.get("I", "N"), 0)
    a = WEIGHTS["A"].get(vector.get("A", "N"), 0)
    if scope == "C":
        pr = {0.85: 0.85, 0.62: 0.68, 0.27: 0.5}.get(pr_base, pr_base)
    else:
        pr = pr_base
    iss = 1 - ((1 - c) * (1 - i) * (1 - a))
    if scope == "U":
        impact = 6.17 * iss
    else:
        impact = 7.52 * (iss - 0.029) - 3.25 * ((iss - 0.02) ** 15)
    exploitability = 8.22 * av * ac * pr * ui
    if impact <= 0:
        return 0.0
    if scope == "U":
        score = min(impact + exploitability, 10)
    else:
        score = min(1.08 * (impact + exploitability), 10)
    import math
    return math.ceil(score * 10) / 10

def severity_label(score: float) -> str:
    if score == 0: return "None"
    if score < 4: return "Low"
    if score < 7: return "Medium"
    if score < 9: return "High"
    return "Critical"

def main():
    if len(sys.argv) < 2:
        print("usage: python cvss_calculator.py CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N")
        sys.exit(1)
    vector_str = sys.argv[1]
    vector = parse_vector(vector_str)
    score = compute_cvss(vector)
    label = severity_label(score)
    print(f"Vector: {vector_str}")
    print(f"Score: {score}")
    print(f"Severity: {label}")

if __name__ == "__main__": main()
