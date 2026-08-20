import unittest

from src.classification_engine import score_system


class ClassificationEngineTests(unittest.TestCase):
    def test_high_risk_valuation_system(self):
        record = {
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
        result = score_system(record)
        self.assertEqual(result.tier, "High")
        self.assertGreaterEqual(result.score, 31)

    def test_low_risk_marketing_system(self):
        record = {
            "decision_impact": "Marketing content generation",
            "financial_impact": "Low",
            "regulatory_impact": "Medium",
            "sensitive_data": "No",
            "autonomy_level": "1",
            "explainability_challenge": "Medium",
            "third_party": "Yes",
            "data_cross_border": "Yes",
            "regions": "UAE|UK|EU",
            "personal_data": "Yes",
            "ai_type": "GenAI/LLM",
        }
        result = score_system(record)
        self.assertIn(result.tier, {"Moderate", "High"})
        self.assertIn("Generative AI", result.regulatory_flags)

    def test_valuation_has_material_financial_flag(self):
        record = {
            "decision_impact": "Valuation decision support",
            "financial_impact": "High",
            "regulatory_impact": "High",
            "sensitive_data": "Yes",
            "autonomy_level": "2",
            "explainability_challenge": "High",
            "third_party": "No",
            "data_cross_border": "No",
            "regions": "UK",
            "personal_data": "No",
            "ai_type": "Predictive ML",
        }
        result = score_system(record)
        self.assertIn("Material financial impact", result.regulatory_flags)


if __name__ == "__main__":
    unittest.main()
