# NovaCommerce Enterprise Data & Knowledge Agent

NovaCommerce is a learning project for building a production-minded GenAI and agentic AI system using public and synthetic data.

The project will evolve gradually across retrieval, RAG, tool use, agents, LangGraph, MCP, memory, evaluation, security, APIs, containers, and CI/CD.

## Current Stage

Stage 1 — repository and LLM application foundations.

The repository includes a small LLM CLI with an OpenAI provider,
separate configuration, Pydantic-validated JSON, and offline tests.

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

Show the CLI help:

```bash
uv run --locked novacommerce --help
```

For API configuration and questions, see the LLM CLI section below.

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


## LLM CLI

Install the project and its development dependencies:

```bash
uv sync --locked
```

Create a local `.env` using `.env.example` as the template.
Set `OPENAI_API_KEY` to your API key and select `OPENAI_MODEL`.

Run a question with its supporting information:

```bash
uv run --locked --env-file .env novacommerce "Policy: Orders delivered more than two days late qualify for a refund. Order: Three days late. Question: Does it qualify?"
```

The command prints JSON containing:
- `answer`: a string
- `needs_more_information`: a boolean

Pydantic validates the fields and their types. It does not guarantee
that the answer is factually correct.

Run the automated tests without making API calls:

```bash
uv run --locked pytest -q
```

Check application types:

```bash
uv run --locked --with mypy mypy src/novacommerce
```