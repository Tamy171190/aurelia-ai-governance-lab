# Project 13 - Multi-Jurisdictional AIMS & Regulatory Mapping

## Objective

Build the regulatory mapping layer that sits across Aurelia's entire AI Governance Management System (AIMS).

The purpose is not to create four disconnected compliance programmes. The purpose is to identify which requirements apply to each AI system, harmonise common requirements into a single control where possible, and retain jurisdiction-specific enhancements where necessary.

## Jurisdictions and Frameworks

### Jurisdictions

- European Union
- United Kingdom
- Singapore
- United Arab Emirates

### Cross-framework baselines

- ISO/IEC 42001
- NIST AI Risk Management Framework

### Singapore enhancement

The design also recognises Singapore's Model AI Governance Framework and its 2026 guidance for agentic AI where relevant to a use case.

## Control Ceiling Method

For each governance requirement:

1. Identify the AI system, activity, entity, data flow and operating jurisdictions.
2. Determine which regulatory and framework requirements are potentially applicable.
3. Record the applicability basis and any uncertainty.
4. Translate each applicable requirement into a control expectation.
5. Compare overlapping control expectations.
6. Establish the **highest applicable control requirement** as the harmonised Aurelia baseline where practical.
7. Add jurisdiction-specific enhancements where the baseline is insufficient.
8. Link the control to evidence, testing and monitoring.

The control ceiling is therefore a **control-design principle**, not a statement that the strictest regulation automatically applies in every geography.

## Control Architecture

**Requirement -> Applicability -> Control Requirement -> Control Objective -> Control Activity -> Evidence -> Test -> Finding -> Remediation -> Monitoring**

## Applicability Statuses

- Applicable
- Potentially applicable
- Assess applicability
- Not applicable
- Jurisdiction-specific enhancement
- Internal AIMS baseline

## Example

**Risk:** Insufficient human oversight

**EU:** assess applicable human-oversight requirements based on system role and scope.

**UK:** translate applicable regulatory principles and sector expectations into accountability and oversight controls.

**Singapore:** incorporate appropriate human involvement and accountability, including agentic-AI checkpoints where relevant.

**UAE:** assess applicable UAE governance, data and sector requirements based on deployment and processing context.

**ISO/IEC 42001:** establish documented AIMS responsibilities, risk treatment and operational controls.

**NIST AI RMF:** GOVERN / MAP / MANAGE.

**Aurelia control:** Define qualified human oversight, intervention authority, override criteria, escalation routes, training and evidence of effective review.

## Deliverables

- Master regulatory-to-control mapping matrix
- Jurisdictional applicability matrix
- Control ceiling assessment
- Jurisdiction-specific enhancement register
- Evidence mapping
- Control testing linkage
- Exception and legal-review tracker

## Important Note

This is a fictional learning and demonstration environment. It is not legal or regulatory advice. Regulatory applicability must be validated against current official sources for the specific entity, activity, AI system and jurisdiction before real-world use.
