
# IntegrityFlow Agent Orchestrator (Local LLM, Free)

IntegrityFlow is a **simple agentic system** built to understand how modern AI systems are designed.
It runs **fully on a local LLM using Ollama**, so **no paid API keys are required**.

This project focuses on **learning**, **clean architecture**, and **agent orchestration**.

---

## What This Project Does

The system takes a user query and processes it through a clear pipeline:

1. **Guardrails** – validate and block unsafe or risky input  
2. **Router** – decide which agent should handle the query  
3. **Agent** – build a role-specific prompt  
4. **Local LLM (Ollama)** – generate the response  
5. **Tracing** – record what happened at each stage  

---

## Why This Project Exists

This project demonstrates:

- how to build an agentic system from scratch  
- separation of concerns (core logic vs agents vs data)  
- safe input handling using guardrails  
- routing requests to specialist agents  
- observability using simple tracing  
- running LLM systems **locally and for free**

It avoids heavy frameworks on purpose, to make the learning clear.

---

## High-Level Flow
```
User Input
↓
Guardrails (allow / block)
↓
Router (coding / explainer / fallback)
↓
Agent (builds prompt)
↓
LLM Client (Ollama)
↓
Response + Trace Events

```
---

## Project Structure
```
src/
app.py # CLI entry point
agents/
base.py # BaseAgent interface
coding_agent.py # Coding specialist agent
explainer_agent.py # Explainer specialist agent
core/
types.py # Pydantic data models
guardrails.py # input validation logic
routers.py # keyword-based routing
llm_client.py # Ollama HTTP client
orchestrator.py # connects all stages
tracer.py # collects trace events
tests/
test_guardrails.py
test_router.py

```

---

## Requirements

- Python **3.10+**
- Ollama installed locally
- A local model pulled (example: `llama3.1:8b`)

---

## Setup Instructions

### 1) Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install Dependencies
```bash
pip install pydantic requests pytest
```

### 3) Start Ollama and pull a model
```bash
ollama run llama3.1:8b

```

## RUN THE APPLICATION

From the project roor:

```bash
python3 -m src.app
```
Type "exit' to quit

## Example Inputs

- Explain what routing is
- I got a python error and traceback
- drop table users (blocked by guardrails)

## Tracing

Each request produces trace events, such as:
- guardrails status (ok / blocked)
- router decision and confidence
- which agent was used
- fallback or error cases
- Tracing helps understand how the system made decisions.

