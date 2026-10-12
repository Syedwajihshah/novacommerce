# GenAI & Agentic AI Mastery — Learning Progress

This file is the durable learning checkpoint for the NovaCommerce
AI Engineering & Agentic Systems Mastery program.

---

## Current position

**Last updated:** 2026-10-12  
**Current stage:** Stage 1 — AI-native engineering + LLM application foundations  
**Current day:** Day 1 — Environment audit and repository contract  
**Day status:** PARTIAL  
**Overall active days completed:** 0 / 60  
**Current project version:** V0  
**Current Git branch:** main  
**Latest commit SHA:** 4409dcc  
**Open issue / PR:** PR #2 merged; Issue #1 closed by PR

### Current focus

- Complete the remaining Day-1 progress-record and GitHub board requirements.

### Strongest current areas

- Python environment isolation and `uv` workflow
- Git feature-branch / PR workflow
- Repository structure and development contract
- Codex versus repository instructions versus application runtime

### Weakest / uncertain areas

- `pyproject.toml` versus `uv.lock` initially required additional clarification
- pytest discovery and output capture initially required additional clarification
- Reinforce both concepts through future hands-on use

### Next exact action

- Satisfy the Day-1 GitHub issue-board requirement, then rerun CHECKPOINT.

---

# Daily checkpoints

## Day 01 — Environment audit and repository contract

**Date:** 2026-10-12  
**Stage:** Stage 1 — AI-native engineering + LLM application foundations  
**Status:** PARTIAL

### 1. Concepts I can now explain

- Why Ubuntu's system Python should not be modified for project development
- How `uv` manages the project Python environment and dependencies
- Difference between `pyproject.toml`, `uv.lock`, and `.venv`
- How pytest discovers test files and test functions
- Purpose of `AGENTS.md`
- Difference between Codex, repository instructions, Git/GitHub, and application runtime
- Basic feature-branch → review → pull-request → merge workflow

### 2. What I implemented

- Bootstrapped the NovaCommerce Python package
- Configured Python 3.12 with `uv`
- Created `src/`, `tests/`, and `docs/decisions/`
- Added a pytest smoke test
- Added `.env.example` and Git secret-ignore rules
- Added repository-level `AGENTS.md`
- Added README and project metadata
- Created environment documentation and ADR-001
- Exercised Codex in read-only repository-inspection mode

### 3. Artifact / evidence produced

- `AGENTS.md`
- `.env.example`
- `README.md`
- `pyproject.toml`
- `uv.lock`
- `tests/test_smoke.py`
- `docs/environment.md`
- `docs/decisions/ADR-001-python-environment.md`
- GitHub Issue #1
- Pull Request #2

### 4. Evidence and measurements

**Tests:** `uv run pytest -q` → 1 passed  
**Application smoke check:** `uv run novacommerce` → `Hello from novacommerce!`  
**Git validation:** `git diff --check` → no errors  
**Repository state:** `main` synchronized with `origin/main`; clean working tree  
**GPU baseline:** NVIDIA GeForce RTX 2060, 6 GB VRAM  
**Project Python:** Python 3.12.15

### 5. Knowledge-check result

Questions/tasks I could answer:

- Why system Python and project Python should remain separate
- What `.venv` represents
- Difference between `pyproject.toml` and `uv.lock`
- What `uv add`, `uv add --dev`, `uv sync`, and `uv run` do
- How pytest finds `test_smoke.py`
- Why `AGENTS.md` exists
- Why Codex, Git/GitHub, repository instructions, and the runtime are separate layers

Questions/tasks I initially struggled with:

- Exact distinction between `pyproject.toml` and `uv.lock`
- pytest test discovery
- pytest output capture with `capsys`

These were remediated through explanation and hands-on examples.

### 6. Weaknesses / unresolved questions

- Reinforce dependency-resolution concepts through future dependency changes
- Reinforce pytest fixtures and discovery through additional tests
- GitHub issue-board/project requirement still needs to be completed

### 7. Important engineering decisions

- Keep Ubuntu system Python unchanged
- Use Python 3.12 for NovaCommerce
- Use `uv` for Python/environment/dependency management
- Keep dependencies isolated in `.venv`
- Use feature branches and PR-based delivery
- Use `AGENTS.md` as the repository contract for Codex
- Use only public or synthetic data

### 8. Technology freshness decisions

**Official docs checked:** Yes, before Stage 1  
**Recent UAE market signal checked:** Yes  
**Material change found:** No curriculum redesign required  
**Decision:** Continue with provider-neutral architecture, current Codex workflow, first-principles agent foundations, and production-oriented Git/quality practices.

### 9. Git / GitHub checkpoint

**Issue:** #1 — Day 1: Environment audit and repository contract  
**Branch:** `day1-repository-contract` — merged and deleted  
**Merge commit SHA:** `4409dcc`  
**PR:** #2 — merged into `main`  
**CI status:** Not configured yet; scheduled for a later curriculum stage

### 10. Interview explanation

> Codex is a development assistant, while `AGENTS.md` defines how Codex should work inside this repository. Git tracks local code history and branches, while GitHub provides remote collaboration through issues, pull requests, and reviews. NovaCommerce itself is a separate application runtime and must not depend on Codex being present. Python dependencies are isolated using Python 3.12, `uv`, and a project-specific `.venv`.

### 11. Next exact action

- Complete the Day-1 GitHub issue-board/project requirement and rerun `CHECKPOINT`.

---

# Stage gates

| Stage | Days | Topic | Result |
|---|---:|---|---|
| 1 | 1–5 | AI-native engineering + LLM application foundations | NOT STARTED |
| 2 | 6–10 | Local models, embeddings and semantic search | NOT STARTED |
| 3 | 11–15 | Vector databases and search engineering | NOT STARTED |
| 4 | 16–20 | Production-minded RAG | NOT STARTED |
| 5 | 21–25 | Tools and agents from first principles | NOT STARTED |
| 6 | 26–30 | Agent SDK patterns and guardrails | NOT STARTED |
| 7 | 31–35 | LangGraph orchestration | NOT STARTED |
| 8 | 36–40 | Model Context Protocol (MCP) | NOT STARTED |
| 9 | 41–45 | Memory and multi-agent systems | NOT STARTED |
| 10 | 46–50 | Evals, observability, safety and reliability | NOT STARTED |
| 11 | 51–55 | Production engineering and cloud readiness | NOT STARTED |
| 12 | 56–60 | Capstone, portfolio and interview readiness | NOT STARTED |