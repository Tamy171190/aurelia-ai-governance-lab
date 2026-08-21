# Project 01 — AI Systems Inventory & Risk Classification Engine

## Objective

Build a practical AI systems register and an illustrative risk-classification engine for Aurelia Capital Group.

The project asks a foundational AI Governance question:

> **What AI systems does the organisation use, what do they do, who is accountable for them, where are they used, which governance requirements may apply, and what level of governance should apply?**

## Initial AI Landscape

The inventory covers 20 synthetic use cases across Aurelia's UK, EU, Singapore and UAE footprint.

The inventory intentionally contains a mixture of lower, moderate and higher governance needs. A high illustrative score does **not** automatically mean that a system is legally classified as high risk under a particular regulation.

## Multi-Jurisdiction Design

Each inventory record should support assessment against:

- EU AI Act applicability
- UK AI governance and relevant regulatory expectations
- Singapore AI governance expectations, including IMDA guidance where relevant
- UAE AI governance and applicable data or sector requirements
- ISO/IEC 42001 AIMS controls
- NIST AI RMF GOVERN, MAP, MEASURE and MANAGE functions

The inventory captures geography and processing information first. Legal applicability is then assessed rather than inferred solely from the presence of a country name.

## Planned Inventory Attributes

The register will capture:

- System identity and purpose
- Business owner and technical owner
- AI type and model/provider information
- Deployment and processing geography
- Users and affected populations
- Decision impact and autonomy
- Personal and sensitive data
- Financial and regulatory impact
- Third-party dependency
- Explainability and transparency challenges
- Human oversight
- Cross-border processing
- Framework applicability indicators
- Governance tier
- Control ceiling
- Evidence and review status

## Control Ceiling Principle

Where multiple applicable frameworks address the same risk, the AIMS should establish a harmonised control that meets the **highest applicable control requirement** where practical. Jurisdiction-specific requirements that cannot be harmonised remain explicit enhancements or exceptions.

This is a governance design principle, not a claim that the strictest law automatically applies in every jurisdiction.

## Planned Classification Approach

The classification engine will use an **illustrative, portfolio-specific methodology** rather than claiming that numerical thresholds are prescribed by any regulation or standard.

Potential risk factors include:

- Impact on individuals
- Investment or financial decision impact
- Regulatory significance
- Sensitive or confidential data
- Autonomy
- Potential financial harm
- Potential reputational harm
- Third-party dependency
- Explainability challenges
- Cross-border processing

The project distinguishes between **illustrative risk scoring**, **framework applicability**, and **legal/regulatory classification**.

## Next Build Steps

1. Maintain the synthetic inventory dataset.
2. Define the data dictionary and applicability fields.
3. Establish the scoring methodology.
4. Implement the classification engine in Python.
5. Add jurisdictional and framework flags.
6. Add validation and test cases.
7. Stress-test borderline scenarios.
8. Document assumptions and limitations.
9. Connect outputs to the risk, control, vendor, evidence and assurance projects.
