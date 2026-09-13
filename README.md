# SupportOps — Software Incident & Technical Ticket Troubleshooting Platform

A portfolio-ready support operations platform built with Python, FastAPI, SQLite, SQLAlchemy, HTML/CSS/JavaScript, REST APIs, and Linux-oriented troubleshooting workflows.

## Features
- Technical ticket creation, tracking, filtering, priority, assignment, requester and support-channel metadata
- Rule-based troubleshooting for performance, permissions, disk, and database issues
- Automatic severity and category suggestions
- Resolution notes and customer-facing response templates
- Ticket status lifecycle with open/resolved workflow
- REST API and browser dashboard
- Support metrics for ticket volume, priority, resolution rate, and response completeness
- Seed data and deterministic tests

The ticket model is designed around common service-desk workflows and can be mapped conceptually to Jira Service Management, ServiceNow, or similar ticket queues; this project does not claim a live integration with those products.

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
Deterministic tests cover troubleshooting rules and response consistency. Resume percentages should only be claimed after reproducing the corresponding benchmark scenarios.
