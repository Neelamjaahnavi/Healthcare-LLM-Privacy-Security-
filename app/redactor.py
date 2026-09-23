from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

class PHIRedactor:
    def __init__(self):
        # Initialize Presidio engines for PII/PHI detection & redaction
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

    def redact_phi(self, text: str):
        # Analyze text for PII/PHI entities (e.g., PERSON, PHONE_NUMBER, US_SSN, EMAIL)
        results = self.analyzer.analyze(text=text, entities=[], language="en")
        
        # Redact/Anonymize detected entities
        anonymized_result = self.anonymizer.anonymize(
            text=text,
            analyzer_results=results
        )
        
        detected_types = list(set([res.entity_type for res in results]))
        return anonymized_result.text, detected_types
