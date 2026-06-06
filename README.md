# AI SDLC Assistant

A multi-agent Software Development Life Cycle (SDLC) assistant built using Spec Driven Development, Git, automated testing, and GitHub Actions.

This project demonstrates how requirements, design, task planning, implementation, testing, and CI/CD can be organized into a structured development workflow.

---

## Project Overview

AI SDLC Assistant is a learning project that simulates how AI agents can collaborate during software development.

The system follows a structured Software Development Life Cycle (SDLC) and uses dedicated agents for each phase of development.

### Objectives

* Demonstrate Spec Driven Development
* Practice Git branching and version control
* Implement agent-based architecture
* Automate testing using Pytest
* Automate validation using GitHub Actions
* Prepare for future LLM integration

---

## SDLC Workflow

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

Each phase is tracked through Git commits and can be developed independently using feature branches.

---

## System Architecture

User
↓
Orchestrator
↓
Requirements Agent
↓
Design Agent
↓
Task Planning Agent
↓
Code Generation Agent
↓
LLM Interface

### Component Responsibilities

#### Requirements Agent

* Collects project requirements
* Produces requirement specifications

#### Design Agent

* Generates high-level architecture
* Defines system components

#### Task Planning Agent

* Breaks requirements into implementation tasks
* Creates development roadmap

#### Code Generation Agent

* Produces starter code structures
* Generates implementation templates

#### Orchestrator

* Coordinates communication between agents
* Controls workflow execution

#### LLM Interface

* Provides abstraction layer for future AI model integration
* Supports future integration with Ollama, Llama, and other LLMs

---

## Project Structure

```text
ai-sdlc-assistant/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
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
│   └── test_design_agent.py
│
└── README.md
```

---

## Technologies Used

* Python 3.12
* Git
* GitHub
* GitHub Actions
* Pytest
* Agent-Based Architecture
* Spec Driven Development

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/akashrams2002/ai-sdlc-assistant.git
cd ai-sdlc-assistant
```

Run the application:

```bash
python src/main.py
```

---

## Running Tests

Execute all automated tests:

```bash
pytest
```

Expected output:

```text
2 passed
```

---

## GitHub Actions

This repository includes a GitHub Actions workflow.

The workflow automatically:

1. Checks out the repository
2. Installs Python
3. Installs project dependencies
4. Runs Pytest
5. Reports test results

This ensures code quality is automatically validated whenever code is pushed to GitHub.

---

## Development Workflow

The project follows a feature-branch strategy:

```text
main
│
├── feature/requirements
├── feature/requirements-agent
├── feature/design-agent
├── feature/task-agent
├── feature/code-agent
├── feature/tests
└── feature/readme
```

Each feature is developed independently and merged into the main branch after validation.

---

## Future Enhancements

### Phase 2

* Real agent communication
* Dynamic workflow execution
* Improved orchestration logic

### Phase 3

* Ollama integration
* Llama 3 support
* Mistral support
* Prompt engineering framework

### Phase 4

* Automatic requirements generation
* Automatic design generation
* Automatic code generation
* Multi-agent collaboration

### Phase 5

* Web UI
* Project dashboard
* Export to Markdown/PDF
* End-to-end SDLC automation

---

## Learning Outcomes

This project demonstrates:

* Spec Driven Development
* Software Development Life Cycle (SDLC)
* Git branching strategy
* Automated testing
* Continuous Integration (CI)
* GitHub Actions
* Agent-based system design
* Future AI/LLM integration patterns

---

## Author

Akash Rams

Built as a hands-on learning project to understand SDLC, Git, GitHub Actions, Agent Architecture, and AI-assisted software development.
