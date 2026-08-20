# Project 01 — AI Systems Inventory & Risk Classification Engine

## Objective

Build a practical AI systems register and an illustrative risk-classification engine for Aurelia Capital Group.

The project asks a foundational AI Governance question:

> **What AI systems does the organisation use, what do they do, who is accountable for them, and what level of governance should apply?**

## Initial AI Landscape

The first inventory will cover 12 core use cases:

| ID | AI System | Function | AI Type | Primary Region |
|---|---|---|---|---|
| AI-001 | Aurelia Research Copilot | Investment Research | GenAI / LLM | UK |
| AI-002 | ValuAI | Private Equity Valuation | Predictive / ML | UK |
| AI-003 | NAVAssist | Fund Administration | ML / Rules + AI | EU |
| AI-004 | InvestorGPT | Investor Reporting | GenAI / LLM | UK |
| AI-005 | KYC Sentinel | Compliance | Predictive AI | EU |
| AI-006 | Aurelia ClientBot | Investor Relations | GenAI / LLM | UAE |
| AI-007 | ContractIQ | Legal / Procurement | GenAI / NLP | Singapore |
| AI-008 | TalentAI | HR | ML | UK |
| AI-009 | CodeAssist | Technology | GenAI / LLM | Global |
| AI-010 | MarketingGen | Marketing | GenAI / LLM | UAE |
| AI-011 | PortfolioWatch | Portfolio Management | Predictive AI | UK/EU |
| AI-012 | VendorGPT | Enterprise AI Platform | Third-party LLM | Global |

## Planned Inventory Attributes

The register will capture identification, ownership, AI characteristics, data characteristics, impact, geography, regulatory indicators, human oversight, third-party dependency, documentation and governance status.

## Planned Classification Approach

The classification engine will use an **illustrative, portfolio-specific methodology** rather than claiming that the numerical thresholds are prescribed by any regulation or standard.

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

The project will distinguish between **risk scoring** and **regulatory classification**, recognising that a numerical risk score does not automatically determine legal classification.

## Next Build Steps

1. Create the synthetic inventory dataset.
2. Define the data dictionary.
3. Establish the scoring methodology.
4. Implement the classification engine in Python.
5. Add validation and test cases.
6. Stress-test borderline scenarios.
7. Document assumptions and limitations.
8. Connect outputs to future risk-assessment and control projects.
