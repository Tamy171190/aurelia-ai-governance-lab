# AI Classification Engine Prototype

A lightweight rule-based prototype showing how an AI Governance team could translate governance attributes into an initial risk classification and control profile.

## Purpose

This is an illustrative governance prototype, not a legal or regulatory determination engine. It demonstrates traceable decision logic that can be challenged, tested and improved.

## Input

The prototype considers:

- AI system purpose
- Financial-services impact
- Whether decisions affect customers or investors
- Personal-data use
- Human oversight
- External model or vendor dependency
- Potentially high-impact outcomes
- Deployment jurisdictions

## Output

The engine produces:

- Initial governance tier
- Decision rationale
- Recommended governance actions
- Jurisdictional review flags
- A reminder that legal applicability must be separately assessed

## Example

`InvestorGPT`, used by investment professionals to generate client-facing draft commentary, is treated as a high-governance-attention use case because of financial-services context, potential external impact, GenAI characteristics and the need for meaningful human review.

## Design principle

The prototype deliberately separates:

**Classification -> Regulatory applicability -> Control requirements**

A system is not classified as legally regulated merely because a rule fires in this prototype. Legal applicability depends on the relevant entity, activity, system role, data, affected persons and jurisdiction.

## Relationship to the Excel Lab

The Excel workbook demonstrates the operational governance record. This prototype demonstrates the decision logic that could sit behind the classification workflow.
