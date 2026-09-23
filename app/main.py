from fastapi import FastAPI, HTTPException, status
from app.models import SanitizeRequest, SanitizeResponse
from app.redactor import PHIRedactor
from app.guardrail import SecurityGuardrail

app = FastAPI(
    title="Healthcare LLM Privacy & Security Guardrail API",
    description="HIPAA-compliant proxy for scrubbing PHI/PII and detecting prompt injections prior to LLM processing.",
    version="1.0.0"
)

redactor = PHIRedactor()
guardrail = SecurityGuardrail()

@app.get("/")
def root():
    return {"status": "healthy", "service": "Healthcare LLM Guardrail API"}

@app.post("/api/v1/sanitize", response_model=SanitizeResponse)
def sanitize_prompt(payload: SanitizeRequest):
    # 1. Check prompt injection & security validation
    is_safe, message = guardrail.validate_prompt(payload.prompt)
    if not is_safe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": message, "flagged": True}
        )
    
    # 2. Redact PHI/PII entities
    sanitized_text, entities = redactor.redact_phi(payload.prompt)
    
    return SanitizeResponse(
        original_prompt=payload.prompt,
        sanitized_prompt=sanitized_text,
        detected_entities=entities,
        is_safe=True,
        security_flag=None
    )
