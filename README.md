<p align="center">
  <img src="assets/brand/hero.svg" alt="Bug Bounty Guide" width="100%">
</p>

<p align="center">
  <a href="SKILL.md"><img alt="AgentSkill" src="https://img.shields.io/badge/🤖_AgentSkill-Ready-111827?style=for-the-badge&labelColor=0d1117"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/📜_CC_BY_4.0-c9a96e?style=for-the-badge&labelColor=b8860b&color=f5d07a"></a>
  <a href="docs/workflows/openclaw-quickstart.md"><img alt="Quickstart" src="https://img.shields.io/badge/⚡_Quickstart-5_min-2563eb?style=for-the-badge&labelColor=1d4ed8"></a>
  <a href="docs/enterprise/compliance-mapping.md"><img alt="Enterprise" src="https://img.shields.io/badge/🏢_Enterprise-NIST_|_ISO_|_SOC2-16a34a?style=for-the-badge&labelColor=15803d"></a>
</p>

<p align="center">
  <strong>Bug Bounty Guide</strong> transforms vague <em>"scan this target"</em> requests into controlled, auditable research engagements.<br>
  AI agents receive an operational contract: authorize → map → model → test → validate → report → stop.
</p>

<p align="center">
  <img src="assets/brand/workflow.svg" alt="Seven-phase operational workflow" width="100%">
</p>

---

## 🏗️ What Makes It Different

<table>
<tr>
<td width="50%" valign="top">

### 🛡️ Fail-Closed Authorization
`scope_guard.py` blocks incomplete or unsafe manifests before any traffic is sent. A hostname is never authorization.

### 📦 Artifacts Over Improvisation
Every phase produces reviewable output before the next transition. No silent jumps.

### 🎯 Falsification First
Validator tries to disprove every candidate before submission. Quality over volume.

</td>
<td width="50%" valign="top">

### 🔒 One Controlled Executor
Multi-agent teams cannot silently multiply target traffic. One agent sends requests.

### ✅ Minimum Viable Proof
Research stops when impact is safely demonstrated. Not one request more.

### 📊 Evidence-Driven
Every finding carries redacted evidence, CWE/OWASP mapping, and CVSS scoring.

</td>
</tr>
</table>

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/0x4riff/BugBountyGuide.git
cd BugBountyGuide

# 2. Validate scope
python scripts/scope_guard.py scope.example.json

# 3. Scaffold engagement
python scripts/bbg.py init acme

# 4. Score a finding
python scripts/bbg.py score engagements/acme/findings/HYP-001.json

# 5. Generate report
python scripts/bbg.py report acme
```

📖 **Full setup:** [OpenClaw Quickstart](docs/workflows/openclaw-quickstart.md)

---

## 🧰 Unified CLI

One entry point for everything:

| Command | Description |
|:--------|:------------|
| `bbg.py init <name>` | Scaffold engagement folder with scope.json + findings.json |
| `bbg.py validate <name>` | Run scope guard on engagement |
| `bbg.py score <file>` | Compute risk score (0–15) for a finding |
| `bbg.py report <name>` | Generate markdown report from findings |
| `bbg.py list` | List all engagements with status |
| `bbg.py dashboard` | Global summary across all engagements |
| `bbg.py export <name>` | Export findings to CSV |
| `bbg.py import <name> <file>` | Import findings from JSON |

```bash
python scripts/bbg.py dashboard
# engagements: 3
# total findings: 12
# avg risk score: 7.2/15
```

---

## 📐 Visual Dashboards (Canvas)

Apple-style interactive dashboards for OpenClaw Canvas:

| Dashboard | Purpose | File |
|:----------|:--------|:-----|
| **Control Center** | Generate scope.json manifests with instant validation | [`assets/canvas/dashboard.html`](assets/canvas/dashboard.html) |
| **Progress Tracker** | Monitor engagement phases, findings, risk scores | [`assets/canvas/progress.html`](assets/canvas/progress.html) |
| **Attack Surface Map** | Visual endpoint risk heatmap | [`assets/canvas/surface-map.html`](assets/canvas/surface-map.html) |

```bash
# Launch on OpenClaw
python scripts/canvas_launcher.py
# Then in your session:
canvas(action='present', url='/__openclaw__/canvas/bug_bounty_guide_dashboard.html')
```

---

## 🔬 Testing Toolkit

### CVSS Calculator
```bash
python scripts/lib/cvss_calculator.py CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
# Score: 6.3 / Severity: Medium
```

### Evidence Manager
```bash
python scripts/lib/evidence_manager.py capture request-001 < response.txt
python scripts/lib/evidence_manager.py list
```

### Test Runner (rate-limited)
```bash
python scripts/lib/test_runner.py engagements/acme/findings/HYP-001.json 2.0
```

### Time Tracker
```bash
python scripts/lib/time_tracker.py acme start recon
python scripts/lib/time_tracker.py acme summary
```

### Scope Discovery
```bash
python scripts/lib/scope_discovery.py scope.example.json
```

### Auto-Deploy
```bash
python scripts/lib/auto_deploy.py engagements/acme 0x4riff/my-tracker
```

---

## 📚 Knowledge Base

Deep-dive articles per vulnerability class with CWE/OWASP mapping, safe payloads, remediation, and CVSS scoring:

| Article | CWE | OWASP | CVSS |
|:--------|:----|:------|:-----|
| [IDOR & Access Control](docs/kb/idor-access-control.md) | CWE-639 | A01:2021 | 6.5 |
| [SSRF](docs/kb/ssrf.md) | CWE-918 | A10:2021 | 7.2 |
| [Injection (XSS/SQLi)](docs/kb/injection.md) | CWE-79/89/78 | A03:2021 | 6.1 |
| [Business Logic](docs/kb/business-logic.md) | CWE-840 | A04:2021 | 5.4 |
| [API Security](docs/kb/api-security.md) | CWE-284/306 | A01/A05 | 6.5 |

---

## 🏢 Enterprise Compliance

| Framework | Controls | Mapping |
|:----------|:---------|:--------|
| **NIST SP 800-53 Rev. 5** | RA-5, CA-2, CA-8, AC-6, SI-4 | [compliance-mapping.md](docs/enterprise/compliance-mapping.md) |
| **ISO/IEC 27001:2022** | A.5.8, A.8.8, A.8.20, A.8.24 | [compliance-mapping.md](docs/enterprise/compliance-mapping.md) |
| **SOC 2 Type II** | CC7.1, CC4.1 | [compliance-mapping.md](docs/enterprise/compliance-mapping.md) |
| **CI/CD Pipeline** | GitHub Actions integration | [cicd-playbook.md](docs/enterprise/cicd-playbook.md) |

---

## 🧩 Reference Toolkit

| Resource | Description |
|:---------|:------------|
| [Glossary](docs/reference/glossary.md) | Precise definitions for agents and humans |
| [Cheatsheet](docs/reference/cheatsheet.md) | Fast pre-flight and reporting checklist |
| [Test Plan Template](docs/reference/test-plan-template.md) | Copy-ready per-hypothesis plan |
| [False-Positive Database](docs/database/false-positives.json) | 10 common patterns with verdict and controls |
| [Finding Schema](schemas/finding-schema.json) | JSON Schema with CWE/OWASP/CVSS fields |
| [Scope Schema](schemas/scope-schema.json) | Machine-readable scope validation rules |
| [Changelog](CHANGELOG.md) | Version history |

---

## 🗂️ Repository Architecture

```
BugBountyGuide/
├── SKILL.md                         # Agent entry point and mandatory gates
├── scripts/
│   ├── bbg.py                       # Unified CLI (init/validate/score/report/list/export)
│   ├── scope_guard.py               # Deterministic authorization check
│   ├── canvas_launcher.py           # Canvas dashboard deployer
│   └── lib/
│       ├── cvss_calculator.py       # CVSS v3.1 scoring
│       ├── evidence_manager.py      # Capture, hash, redact evidence
│       ├── scope_discovery.py       # Wildcard resolution
│       ├── test_runner.py           # Rate-limited hypothesis testing
│       ├── time_tracker.py          # Per-phase time logging
│       └── auto_deploy.py           # GitHub issue sync
├── schemas/
│   ├── scope-schema.json            # Scope manifest schema
│   └── finding-schema.json          # Finding record schema (CWE/OWASP/CVSS)
├── docs/
│   ├── 00-09                        # Web/API field guide (10 chapters)
│   ├── kb/                          # Knowledge base per CWE class
│   ├── workflows/                   # Advanced operating model
│   ├── enterprise/                  # NIST/ISO/SOC2 compliance
│   ├── reference/                   # Glossary, cheatsheet, templates
│   └── database/                    # False-positive patterns
├── assets/
│   ├── brand/                       # Hero SVG, workflow diagram
│   ├── canvas/                      # Interactive dashboards (3)
│   ├── engagement-template.md       # Engagement plan template
│   └── report-template.md           # Submission report template
├── checklists/                      # Human review controls (3)
├── references/                      # Agent playbook, validation gates
├── scope.example.json               # Example scope manifest
├── config.json                      # Global research configuration
└── CHANGELOG.md                     # Version history
```

---

## ⚙️ Operating Model

```
┌─────────────────────────────────────────────────────────┐
│                    COORDINATOR                           │
│  Owns scope, request budget, transitions, stop decision │
└──────┬──────┬──────┬──────┬──────┬──────┬───────────────┘
       │      │      │      │      │      │
   ┌───▼──┐┌──▼───┐┌─▼────┐┌▼─────┐┌▼────┐┌▼──────┐
   │Scope ││Recon ││Planner││Execu-││Vali-││Report-│
   │Agent ││Agent ││       ││tor   ││dator││er     │
   └──────┘└──────┘└───────┘└──────┘└─────┘└───────┘
   Extract  Passive  Bounded    Alone   Attack  Redact
   policy   inventory experiments sends  assump- evidence
                     traffic    tions
```

**Seven-phase workflow:**
1. **Authorize** — preserve policy evidence and exact boundaries
2. **Map** — inventory only assets with explicit scope match
3. **Model** — identify actors, objects, states, enforcement points
4. **Test** — change one variable using minimum request budget
5. **Validate** — run controls and eliminate alternatives
6. **Report** — separate observation, inference, impact, remediation
7. **Stop** — close after minimum reproducible proof

Advanced detail: [state machine, risk budget, confidence model](docs/workflows/advanced-operating-model.md).

---

## 📖 Field Guide

[Rules](docs/00-rules-of-engagement.md) · [Method](docs/01-methodology.md) · [Recon](docs/02-recon.md) · [Web](docs/03-web-testing.md) · [API/GraphQL](docs/04-api-graphql.md) · [Identity](docs/05-identity.md) · [Business Logic](docs/06-business-logic.md) · [Validation](docs/07-validation.md) · [Reporting](docs/08-reporting.md) · [Tooling](docs/09-tooling.md)

---

## 🚫 Safety Boundary

> **Permission precedes capability.**

**Stop on:** real-user data · credentials · instability · third-party assets · irreversible change · unclear authorization

**Never:** DoS · phishing · credential attacks · persistence · malware · stealth/evasion · secret harvesting · private-network/cloud-metadata probing

*Unless program explicitly authorizes the exact action.*

---

## 🤝 Contributing

Original techniques welcome when they include scope boundary, safe test, controls, false-positive risks, and maintained references. Read [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📜 Attribution & License

Maintained by [0x4riff](https://github.com/0x4riff). Inspired by public security education including OWASP and PortSwigger Web Security Academy. Repository does not copy unlicensed contents from `KingOfBugBountyTips`.

Content licensed under [CC BY 4.0](LICENSE). Educational and authorized security research only.

---

<p align="center">
  <img alt="OpenClaw" src="https://img.shields.io/badge/Built_for_OpenClaw-AgentSkill-111827?style=for-the-badge&labelColor=0d1117">
  <img alt="Method" src="https://img.shields.io/badge/Method-Scope--First-1f6f5f?style=for-the-badge&labelColor=14532d">
  <img alt="Research" src="https://img.shields.io/badge/Research-Authorized_Only-374151?style=for-the-badge&labelColor=1f2937">
</p>
