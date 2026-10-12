# NovaCommerce Enterprise Data & Knowledge Agent

NovaCommerce is a learning project for building a production-minded GenAI and agentic AI system using public and synthetic data.

The project will evolve gradually across retrieval, RAG, tool use, agents, LangGraph, MCP, memory, evaluation, security, APIs, containers, and CI/CD.

## Current Stage

Stage 1 — repository and LLM application foundations.

At this point, the repository contains only the basic Python project structure, environment configuration, tests, documentation, and repository instructions.

## Requirements

- Python 3.12
- `uv`
- Git

## Setup

Create or synchronize the project environment:

```bash
uv sync --locked --python 3.12
```

## Run

Run the current starter CLI:

```bash
uv run novacommerce
```

Expected output:

```text
Hello from novacommerce!
```

## Tests

Run the test suite:

```bash
uv run pytest
```

## Repository Structure

```text
novacommerce/
├── src/novacommerce/     # Application code
├── tests/                # Automated tests
├── docs/                 # Documentation
│   └── decisions/        # Architecture Decision Records
├── AGENTS.md             # Repository instructions for coding agents
├── .env.example          # Environment-variable template
├── pyproject.toml        # Project and dependency configuration
└── uv.lock               # Locked dependency versions
```

## Environment Variables

Copy `.env.example` to `.env` when local configuration is required.

Never commit real API keys or secrets.

## Data Policy

Only public or synthetic data should be used in this repository.

Do not add confidential employer, client, or customer data.

## Development Approach

Changes should be:

- small and explainable
- implemented on feature branches
- tested before commit
- reviewed through Git diffs
- documented when they introduce meaningful architectural decisions

## Current Limitations

NovaCommerce does not yet contain production LLM, retrieval, RAG, agent, database, or API functionality.

Those capabilities will be added incrementally as the project progresses.