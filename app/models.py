from pydantic import BaseModel, Field
from typing import List, Optional

class SanitizeRequest(BaseModel):
    prompt: str = Field(..., example="Patient John Doe (SSN: 123-45-6789) has hypertension and takes Lysinopril 10mg.")

class SanitizeResponse(BaseModel):
    original_prompt: str
    sanitized_prompt: str
    detected_entities: List[str]
    is_safe: bool
    security_flag: Optional[str] = None
