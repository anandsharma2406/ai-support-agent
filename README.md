# ai-support-agent
This project builds an AI agent to automatically process customer support emails.
# AI Customer Support Agent

## Overview
This project builds an AI agent to automatically process customer support emails.

## Features
- Email classification (urgency + topic)
- Response generation
- Escalation logic
- Follow-up handling

## Architecture
Pipeline:
Input → Classification → Retrieval → Response → Decision

## Tech Stack
- Python
- Groq LLM

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Add .env file with API key

3. Run:
python app/main.py

## Output
Results stored in:
outputs/results.json

## Future Improvements
- Vector database (FAISS)
- UI dashboard
- Email integration
