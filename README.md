# SupportOps — Software Incident & Ticket Troubleshooting Platform

A portfolio-ready support operations platform built with Python, FastAPI, SQLite, SQLAlchemy, HTML/CSS/JavaScript, and REST APIs.

## Features
- Ticket creation and tracking
- Rule-based troubleshooting workflow
- Automatic severity/category suggestions
- Resolution notes and customer-facing response templates
- REST API and browser dashboard
- Seed data and tests

## Run

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python seed.py
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 and `/docs` for API documentation.

## Validation
Deterministic tests cover troubleshooting rules and response consistency. The resume percentages should only be claimed after reproducing the corresponding benchmark scenarios.
