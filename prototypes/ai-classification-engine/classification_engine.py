"""Illustrative AI governance classification prototype.

This is a learning/demo engine. It does not determine legal applicability.
"""

from dataclasses import dataclass, asdict
from typing import List


@dataclass
class AISystem:
    system_id: str
    name: str
    financial_services: bool
    customer_or_investor_impact: bool
    personal_data: bool
    generative_ai: bool
    external_model_or_vendor: bool
    material_decision_support: bool
    human_oversight: bool
    jurisdictions: List[str]


def classify(system: AISystem) -> dict:
    """Return an initial governance tier and traceable rationale."""
    score = 0
    reasons = []
    actions = set()

    if system.financial_services:
        score += 1
        reasons.append("Financial-services use case")
        actions.add("Document business owner and risk owner")

    if system.customer_or_investor_impact:
        score += 2
        reasons.append("Potential customer or investor impact")
        actions.add("Assess human oversight and customer impact")

    if system.personal_data:
        score += 1
        reasons.append("Personal-data processing")
        actions.add("Perform data protection and data governance assessment")

    if system.generative_ai:
        score += 1
        reasons.append("Generative AI characteristics")
        actions.add("Assess transparency, output reliability and misuse risks")

    if system.external_model_or_vendor:
        score += 1
        reasons.append("External AI model or vendor dependency")
        actions.add("Perform third-party AI risk assessment")

    if system.material_decision_support:
        score += 2
        reasons.append("Material decision-support capability")
        actions.add("Perform enhanced AI risk assessment and validation")

    if not system.human_oversight:
        score += 2
        reasons.append("No meaningful human oversight identified")
        actions.add("Escalate for human-oversight design before deployment")

    if score >= 7:
        tier = "HIGH"
    elif score >= 4:
        tier = "MEDIUM"
    else:
        tier = "LOW"

    if tier == "HIGH":
        actions.update({
            "Enhanced risk assessment",
            "Documented approval gate",
            "Post-deployment monitoring",
            "Independent assurance consideration",
        })

    return {
        "system": asdict(system),
        "governance_score": score,
        "initial_governance_tier": tier,
        "decision_rationale": reasons,
        "recommended_actions": sorted(actions),
        "jurisdictional_review_required": bool(system.jurisdictions),
        "legal_applicability_note": (
            "This result is an illustrative governance classification only. "
            "Regulatory applicability requires a separate jurisdiction, entity, "
            "activity, system-role and data-flow assessment."
        ),
    }


if __name__ == "__main__":
    investor_gpt = AISystem(
        system_id="AI-004",
        name="InvestorGPT",
        financial_services=True,
        customer_or_investor_impact=True,
        personal_data=False,
        generative_ai=True,
        external_model_or_vendor=True,
        material_decision_support=True,
        human_oversight=True,
        jurisdictions=["UK", "EU", "Singapore", "UAE"],
    )

    import json
    print(json.dumps(classify(investor_gpt), indent=2))
