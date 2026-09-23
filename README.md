# Privacy-Preserving Healthcare LLM Guardrail & PII Redactor

An API proxy built with **FastAPI**, **Microsoft Presidio**, and **Spacy** to enforce HIPAA/PHI data privacy and threat protection before queries are submitted to Large Language Models (LLMs).

## Features
- **PHI / PII Redaction:** Redacts patient names, phone numbers, SSNs, and sensitive data attributes in real time.
- **Prompt Injection Defense:** Scans incoming payloads for malicious prompt injections, jailbreaks, and instructions override.
- **Low-Latency Architecture:** Asynchronous FastAPI endpoints designed for high throughput.
- **Dockerized:** Packaged for deployment to containerized environments like GCP Cloud Run or AWS ECS.

## Project Structure
```text
.
├── app/
│   ├── main.py        # FastAPI entrypoint
│   ├── redactor.py    # PHI Redaction logic using Presidio
│   ├── guardrail.py   # Prompt injection & jailbreak detection
│   └── models.py      # Pydantic schema validation
├── tests/             # Automated test suite
├── Dockerfile         # Deployment container setup
└── requirements.txt
```

# Quickstart

## 1. Local Setup
```
# Clone the repository
git clone [https://github.com/Neelamjaahnavi/healthcare-llm-guardrail.git](https://github.com/Neelamjaahnavi/healthcare-llm-guardrail.git)
cd healthcare-llm-guardrail

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies & spacy language model
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Run application
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs to test endpoints via Interactive Swagger UI.

## 2. Docker Setup
```
docker build -t healthcare-llm-guardrail .
docker run -p 8000:8000 healthcare-llm-guardrail
```

# Testing
```
pytest
```

