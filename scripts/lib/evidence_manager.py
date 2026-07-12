#!/usr/bin/env python3
"""Evidence Manager — Capture, hash, redact, and organize test evidence."""
import json, hashlib, base64, re, sys
from pathlib import Path
from datetime import datetime

EVIDENCE_DIR = Path(__file__).resolve().parent.parent / "engagements" / "evidence"

def _hash(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()[:16]

def capture(name: str, raw: str, redact_patterns: list = None):
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)
    content = raw.encode("utf-8")
    if redact_patterns:
        text = raw
        for pattern in redact_patterns:
            text = re.sub(pattern, "[REDACTED]", text)
        content = text.encode("utf-8")
    h = _hash(content)
    ts = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    fname = f"{ts}-{name}-{h}.json"
    record = {
        "id": h,
        "name": name,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "sha256_full": hashlib.sha256(content).hexdigest(),
        "redacted": bool(redact_patterns),
        "content_b64": base64.b64encode(content).decode("ascii")
    }
    (EVIDENCE_DIR / fname).write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"captured: {fname}")
    return h

def list_evidence():
    if not EVIDENCE_DIR.exists():
        print("no evidence captured")
        return
    for f in sorted(EVIDENCE_DIR.glob("*.json")):
        rec = json.loads(f.read_text(encoding="utf-8"))
        print(f"{rec['id'][:8]} {rec['name']} {rec['timestamp']}")

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "capture":
        name = sys.argv[2] if len(sys.argv) > 2 else "unnamed"
        raw = sys.stdin.read()
        redact = sys.argv[3].split(",") if len(sys.argv) > 3 else None
        capture(name, raw, redact)
    elif cmd == "list":
        list_evidence()
    else:
        print("unknown command")

if __name__ == "__main__": main()
