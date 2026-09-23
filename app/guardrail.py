import re

class SecurityGuardrail:
    def __init__(self):
        # Known prompt injection & jailbreak patterns
        self.injection_patterns = [
            r"ignore previous instructions",
            r"system prompt override",
            r"bypass security constraints",
            r"you are now in developer mode",
            r"dump internal database"
        ]

    def validate_prompt(self, text: str):
        for pattern in self.injection_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return False, f"Security Violation: Prompt Injection / Jailbreak attempt detected ('{pattern}')"
        return True, "Safe"
