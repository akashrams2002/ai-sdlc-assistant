# AI SDLC Assistant

An AI-powered Software Development Life Cycle (SDLC) Assistant built using Python, Groq, Llama 3, Spec Driven Development, Git, automated testing, and GitHub Actions.

This project demonstrates how AI agents can collaborate to generate software requirements, system designs, development tasks, and code skeletons from a simple project idea.

---

# Project Overview

AI SDLC Assistant simulates how AI can assist throughout the Software Development Life Cycle.

The system uses multiple agents that work together to transform a project idea into structured software artifacts.

Example:

Project Idea:
Online Food Delivery App

↓

Requirements Generation

↓

Architecture Design Generation

↓

Task Planning Generation

↓

Code Skeleton Generation

↓

Documentation Output

---

# Features

✅ AI Requirements Generation

✅ AI Architecture Design Generation

✅ AI Task Planning

✅ Code Skeleton Generation

✅ Automatic Documentation Generation

✅ GitHub Actions CI/CD

✅ Automated Testing with Pytest

✅ Multi-Agent Architecture

✅ Spec Driven Development Workflow

---

# Objectives

* Demonstrate Spec Driven Development
* Practice Git branching and version control
* Implement agent-based architecture
* Generate requirements using AI
* Generate system designs using AI
* Generate development tasks using AI
* Automate testing using Pytest
* Automate validation using GitHub Actions

---

# SDLC Workflow

Requirements

↓

Design

↓

Task Planning

↓

Implementation

↓

Testing

↓

CI/CD

Each phase is represented by a dedicated agent and can evolve independently.

---

# System Architecture

User

↓

Orchestrator

↓

AI Requirements Agent

↓

AI Design Agent

↓

AI Task Agent

↓

Code Generation Agent

↓

Documentation Generator

---

# AI Workflow

Project Idea

↓

Requirements Generation (Groq + Llama 3)

↓

Architecture Design Generation

↓

Task Planning Generation

↓

Code Skeleton Generation

↓

Markdown Documentation Output

---

# Component Responsibilities

## Requirements Agent

* Generates software requirements from project ideas
* Uses Groq + Llama 3
* Produces structured requirement lists

## Design Agent

* Generates high-level system architecture
* Produces modules, services, and components
* Uses AI-generated requirements as input

## Task Agent

* Converts architecture into implementation tasks
* Produces development roadmaps
* Generates realistic SDLC activities

## Code Agent

* Converts implementation tasks into starter code structures
* Generates Python class skeletons

## Orchestrator

* Coordinates communication between agents
* Controls end-to-end workflow execution

## LLM Interface

* Provides abstraction layer for AI providers
* Currently integrated with Groq
* Can be extended to OpenAI, Gemini, or Ollama

---

# Project Structure

```text
ai-sdlc-assistant/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── docs/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
│
├── specs/
│   ├── project_vision.md
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
│
├── src/
│   ├── agents/
│   │   ├── requirements_agent.py
│   │   ├── design_agent.py
│   │   ├── task_agent.py
│   │   └── code_agent.py
│   │
│   ├── orchestrator/
│   │   └── orchestrator.py
│   │
│   ├── models/
│   │   └── llm.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_requirements_agent.py
│   ├── test_design_agent.py
│   ├── test_task_agent.py
│   ├── test_code_agent.py
│   └── test_orchestrator.py
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

* Python 3.12
* Groq API
* Llama 3 70B
* Git
* GitHub
* GitHub Actions
* Pytest
* Agent-Based Architecture
* Spec Driven Development

---

# Running the Project

Clone the repository:

```bash
git clone https://github.com/akashrams2002/ai-sdlc-assistant.git
cd ai-sdlc-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure Groq API Key:

```powershell
$env:GROQ_API_KEY="your_api_key"
```

Run the application:

```bash
python -m src.main
```

---

# Generated Documentation

Every execution automatically generates:

```text
docs/
├── requirements.md
├── design.md
└── tasks.md
```

These files contain AI-generated SDLC artifacts.

---

# Running Tests

Execute all tests:

```bash
pytest
```

---

# GitHub Actions

The repository includes a CI pipeline that automatically:

1. Checks out source code
2. Installs dependencies
3. Runs Pytest
4. Reports results

Every push is automatically validated.

---

# Development Workflow

Feature Branch Strategy:

```text
main
│
├── feature/requirements-agent
├── feature/design-agent
├── feature/task-agent
├── feature/code-agent
├── feature/tests
├── feature/project-cleanup
└── feature/ollama-integration
```

Each feature is developed independently and merged after validation.

---

# Future Enhancements

## Phase 2

* Streamlit Web Interface
* Interactive Dashboard
* AI Code Generation using LLMs
* Multi-provider AI support

## Phase 3

* OpenAI Integration
* Google Gemini Integration
* Ollama Local Models
* LangChain Integration

## Phase 4

* Export Documentation to PDF
* Project Planning Dashboard
* Multi-Agent Collaboration Framework
* End-to-End SDLC Automation

---

# Learning Outcomes

This project demonstrates:

* Spec Driven Development
* Software Development Life Cycle (SDLC)
* Git Branching Strategy
* GitHub Actions CI/CD
* Automated Testing
* Agent-Based System Design
* AI Integration using APIs
* Multi-Agent Architecture
* Documentation Automation

---

# Author

Akash Rams

Built as a hands-on learning project to understand SDLC, Git, GitHub Actions, AI Agents, LLM Integration, and AI-assisted software development.
