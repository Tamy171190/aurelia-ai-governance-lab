"""Illustrative AI risk classification engine for the Aurelia Governance Lab.

This is a fictional demonstration methodology. It is not a regulatory classifier.
"""

from dataclasses import dataclass


@dataclass
class ClassificationResult:
    score: int
    tier: str
    regulatory_flags: list[str]
    required_controls: list[str]


def score_system(record: dict) -> ClassificationResult:
    """Calculate an illustrative inherent risk score from inventory attributes."""
    score = 0

    if record.get("decision_impact") in {"Investment research recommendations", "Valuation decision support", "KYC and AML risk scoring", "Client suitability support"}:
        score += 5
    elif record.get("decision_impact") in {"Portfolio risk monitoring and alerts", "NAV exception identification", "Candidate screening support"}:
        score += 4
    else:
        score += 2

    score += 5 if record.get("financial_impact") == "High" else 3 if record.get("financial_impact") == "Medium" else 1
    score += 5 if record.get("regulatory_impact") == "High" else 3 if record.get("regulatory_impact") == "Medium" else 1
    score += 4 if record.get("sensitive_data") == "Yes" else 0
    score += min(int(record.get("autonomy_level", 1)), 3)
    score += 4 if record.get("explainability_challenge") == "High" else 2 if record.get("explainability_challenge") == "Medium" else 1
    score += 3 if record.get("third_party") == "Yes" else 0
    score += 2 if record.get("data_cross_border") == "Yes" else 0

    flags = ["ISO/IEC 42001 AIMS baseline", "NIST AI RMF applicability: GOVERN/MAP/MEASURE/MANAGE"]
    regions = record.get("regions", "")

    if "EU" in regions or "Global" in regions:
        flags.append("EU applicability assessment")
    if "UK" in regions or "Global" in regions:
        flags.append("UK applicability assessment")
    if "Singapore" in regions or "Global" in regions:
        flags.append("Singapore applicability assessment")
    if "UAE" in regions or "Global" in regions:
        flags.append("UAE applicability assessment")
    if record.get("personal_data") == "Yes":
        flags.append("Personal data")
    if record.get("financial_impact") == "High":
        flags.append("Material financial impact")
    if record.get("third_party") == "Yes":
        flags.append("Third-party AI dependency")
    if record.get("ai_type", "").startswith("GenAI"):
        flags.append("Generative AI")
    if record.get("data_cross_border") == "Yes":
        flags.append("Cross-border processing assessment")

    if score >= 31:
        tier = "High"
        controls = [
            "Formal AI risk assessment",
            "Multi-jurisdiction applicability assessment",
            "Documented human oversight",
            "Enhanced technical and governance documentation",
            "Pre-production approval",
            "Ongoing performance and risk monitoring",
            "Incident management process",
            "Third-party assessment where applicable",
            "Independent assurance or audit consideration",
            "Control ceiling assessment across applicable frameworks",
        ]
    elif score >= 21:
        tier = "Moderate"
        controls = [
            "AI risk assessment",
            "Jurisdiction and framework applicability assessment",
            "Named business and technical owner",
            "Documented human oversight",
            "Periodic monitoring",
            "Change management",
        ]
    else:
        tier = "Low"
        controls = [
            "Inventory registration",
            "Jurisdiction and framework applicability check",
            "Named owner",
            "Baseline documentation",
            "Periodic review",
        ]

    return ClassificationResult(score, tier, flags, controls)


def classify_records(records: list[dict]) -> list[dict]:
    """Return inventory records enriched with classification outputs."""
    results = []
    for record in records:
        result = score_system(record)
        enriched = dict(record)
        enriched["inherent_risk_score"] = result.score
        enriched["governance_tier"] = result.tier
        enriched["regulatory_flags"] = "; ".join(result.regulatory_flags)
        enriched["required_controls"] = "; ".join(result.required_controls)
        results.append(enriched)
    return results


if __name__ == "__main__":
    example = {
        "decision_impact": "Valuation decision support",
        "financial_impact": "High",
        "regulatory_impact": "High",
        "sensitive_data": "Yes",
        "autonomy_level": "2",
        "explainability_challenge": "High",
        "third_party": "No",
        "data_cross_border": "Yes",
        "regions": "UK|UAE",
        "personal_data": "No",
        "ai_type": "Predictive ML",
    }
    print(score_system(example))
