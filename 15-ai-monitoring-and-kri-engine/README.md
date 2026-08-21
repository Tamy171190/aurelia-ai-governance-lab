# Project 15: AI Post-Deployment Monitoring and KRI Engine

## Objective

Demonstrate how Aurelia Capital Group monitors AI systems after deployment and converts operational, model, fairness, security, privacy and governance signals into actionable risk indicators.

The project is designed for a financial-services environment and complements the AI inventory, classification, risk assessment, third-party risk and evidence readiness work already in the lab.

## Why this matters

AI governance does not end at approval. A system can become higher risk after deployment because of model drift, data drift, changing user behaviour, degraded performance, emerging bias, vendor changes, incidents or changes in regulatory applicability.

The monitoring model therefore links:

**AI System -> Risk -> KRI -> Threshold -> Evidence -> Escalation -> Remediation -> Reassessment**

## Monitoring domains

1. Model performance
2. Data quality and data drift
3. Fairness and bias
4. Human oversight and override effectiveness
5. Explainability and transparency
6. Privacy and data protection
7. Cybersecurity and adversarial risk
8. Vendor and third-party dependency
9. AI incidents and near misses
10. Regulatory and policy change
11. Control effectiveness
12. Business and customer impact

## Illustrative financial-services scenarios

| System | Monitoring focus | Example KRI |
|---|---|---|
| CVRank Pro | Fairness and performance | Selection-rate disparity |
| NAVAssist | Accuracy and exception detection | False exception rate |
| KYC Sentinel | Risk scoring quality | False positive rate |
| InvestorGPT | Hallucination and human review | Unverified output rate |
| Aurelia ClientBot | Customer impact and escalation | Unresolved high-risk interaction rate |

## Risk thresholds

The engine uses illustrative thresholds to demonstrate governance mechanics. Thresholds are not presented as universal regulatory limits.

- Green: within approved tolerance
- Amber: threshold breached or adverse trend detected
- Red: material breach, significant incident, loss of required oversight or residual risk above appetite

## Cross-framework mapping

The monitoring approach uses the Aurelia control ceiling principle and maps monitoring activities across:

- EU AI Act
- UK AI governance expectations
- Singapore AI governance principles
- UAE AI governance expectations
- ISO/IEC 42001
- NIST AI RMF

Framework mappings are illustrative and should be validated against current official requirements before real-world use.

## Key outputs

- Monitoring register
- KRI library
- Threshold and escalation matrix
- Monthly AI risk monitoring view
- Incident trigger logic
- Evidence requirements
- Reassessment triggers
- Management escalation decisions

## Reassessment triggers

A monitoring event should trigger reassessment where there is a material change to:

- intended purpose or use case
- model or foundation model
- training or input data
- deployment geography
- affected population
- autonomy or human oversight
- vendor or subcontractor
- risk profile
- regulatory applicability
- material incident history

## Assurance perspective

The project is designed to support auditability by retaining evidence of the metric, source, calculation period, threshold, owner, review, decision and remediation outcome.

This is a fictional learning and demonstration environment. It is not legal, regulatory or compliance advice.
