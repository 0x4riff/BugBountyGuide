# Enterprise compliance mapping

This document maps the Bug Bounty Guide framework to global security control architectures, establishing compliance for corporate red teams, internal audit, and automated agent orchestration.

## NIST SP 800-53 Rev. 5

| NIST Control | Description | BBG Implementation |
|---|---|---|
| **RA-5** | Vulnerability Monitoring and Scanning | AI agent passive discovery mapping and structured validation gates. |
| **CA-2** | Control Assessments | Rules of engagement and positive/negative controls for safe validation. |
| **CA-8** | Penetration Testing | Defined scopes, deterministic safety limits, and structured reporting. |
| **AC-6** | Least Privilege | Two-account authorization boundaries and role-based test execution. |
| **SI-4** | System Monitoring | Researcher-specific HTTP identification headers for traffic attribution. |

## ISO/IEC 27001:2022

| Annex A Control | Control Title | BBG Implementation |
|---|---|---|
| **A.5.8** | Contact with authorities | Human-in-the-loop authorization gates and policy validation URL. |
| **A.8.8** | Management of technical vulnerabilities | Redacted evidence collection and standardized remediation reporting. |
| **A.8.20** | Network security | Explicit ban on Cloud metadata and private subnet probing. |
| **A.8.24** | Use of cryptography | Validation gates verifying cryptographic signature enforcement on JWT. |

## SOC 2 Type II (Trust Services Criteria)

### Common Criteria 7.1 (CC7.1)
*The entity meets its commitments related to security by detecting and assessing vulnerability risks.*
- **Scope Manifest Validation**: Pre-flight automated schema check guarantees that AI agents only execute tests that have been reviewed and approved by human coordinators.
- **Hypothesis Isolation**: Eliminates broad scanner runs in favor of targeted experiments, minimizing risk to availability and operational confidentiality.

### Common Criteria 4.1 (CC4.1)
*The entity assigns responsibility and authority for key security roles.*
- **Execution Separation**: Separates the Test Planner from the single traffic Executor. The Executor cannot independently create or modify its own authorization parameters.
