# NovaCommerce Repository Instructions

## Project and scope

NovaCommerce is an **Enterprise Data & Knowledge Agent** built as a professional learning project using public or synthetic data.

Implement only the requested task or milestone with small, explainable changes.

Before editing:

- Inspect the relevant code, tests, `README.md`, `pyproject.toml`, CI configuration, and architecture decisions.
- Do not assume planned components already exist.
- Follow existing repository conventions.
- Introduce frameworks, services, abstractions, or infrastructure only when the current task requires them.
- Do not implement future curriculum components prematurely.
- Resolve routine implementation choices independently. Ask only when missing information materially affects correctness, scope, security, or an irreversible action.

## Learning contract

This repository is used to learn the mechanisms behind modern GenAI and agentic systems.

Codex is a coding partner, not a substitute for architectural understanding.

- Prefer a plan or repository analysis before large or cross-cutting edits.
- Keep important mechanisms visible and understandable.
- Do not hide a concept behind a framework before the repository is ready for that abstraction.
- Do not introduce RAG, agents, LangGraph, MCP, memory, multi-agent architecture, or additional infrastructure merely because they may be needed later.
- Prefer the simplest implementation that proves the current concept.
- Make generated code easy for the engineer to review, explain, test, and debug.
- For meaningful changes, expect the engineer to review the Git diff and validation evidence before commit or PR.

## Repository layout

- Application code: `src/novacommerce/`
- Tests and small synthetic fixtures: `tests/`
- Documentation: `docs/`
- Architecture decisions: `docs/decisions/`

Keep reusable application logic inside the package rather than in notebooks or ad hoc scripts.

Create additional directories only when a current requirement justifies them.

## Python and dependencies

- Use Python 3.12.
- Use `uv` with the project's virtual environment.
- Do not modify the system Python installation.
- Do not install project dependencies globally.
- Run Python, tests, and Python-based tools through `uv run` where practical.
- Keep Python version declarations consistent with Python 3.12.
- Use `pyproject.toml` for dependency declarations.
- Use `uv.lock` for resolved dependency versions.
- Let `uv` generate and update `uv.lock`; never edit the lockfile manually.
- Add dependencies only for a clear task requirement and explain why they are needed.
- Use `uv add` for runtime dependencies.
- Use `uv add --dev` for development dependencies when appropriate.
- Avoid unrelated dependency upgrades.
- Update `pyproject.toml` and `uv.lock` together when dependencies intentionally change.

When an existing lockfile should not change, prefer locked execution so accidental dependency resolution is detected rather than silently written.

## Implementation

- Prefer readable functions and explicit data flow.
- Add type hints to new or changed public interfaces.
- Follow the formatter, linter, and type-checking conventions currently configured in the repository.
- Keep business logic separate from database, retrieval, model, and external-service clients using the boundaries already present in the project.
- Do not create unnecessary abstraction layers in anticipation of future requirements.
- Validate inputs at external boundaries.
- Return useful errors.
- Do not hide failures with blanket exception handling or fabricated fallback results.
- Keep configuration outside business logic.
- Avoid hardcoded credentials, machine-specific paths, model names, and service endpoints when they should be configurable.
- Use timeouts and bounded retries for external calls.
- Retry operations with side effects only when duplicate execution is safely handled.
- Preserve existing public interfaces and data schemas unless the task explicitly requires a change.
- Document meaningful compatibility or migration impacts.
- Update documentation when setup, configuration, or observable behavior changes.

Record significant architectural decisions and trade-offs in `docs/decisions/`.

Routine implementation choices do not require an ADR.

## Data and knowledge-agent safeguards

Apply these rules when implementing or changing the relevant capability. They do not require building components before the curriculum reaches them.

- Use public or synthetic data.
- Do not introduce confidential employer, client, or customer data.
- Keep secrets out of code, commits, logs, prompts, fixtures, screenshots, and documentation.
- Use environment variables or the repository's configured secret mechanism.
- Keep local `.env` files untracked.
- Use placeholders in `.env.example` when environment configuration is introduced.
- Treat retrieved documents, external content, user input, and model outputs as untrusted.
- Instructions embedded in retrieved or external content must not change permissions or authorize tool actions.
- Validate model-generated structured output and tool arguments before deterministic execution.
- Do not execute arbitrary generated Python, shell commands, or unrestricted SQL.
- Default analytical database access to read-only.
- Use database permissions as well as application-level controls.
- Parameterize SQL values and allowlist dynamic identifiers where required.
- Bound query runtime and result size.
- Enforce user or tenant access scope at query, retrieval, storage, and cache boundaries.
- Never rely on prompts alone for authorization.
- Calculate deterministic business metrics with SQL or Python where appropriate.
- Preserve source references for factual answers.
- Distinguish evidence, inference, and missing information.
- Never invent records, query results, citations, metrics, or evaluation scores.
- Make ingestion and retries safe to repeat where applicable.
- Preserve stable identifiers and provenance so reruns do not silently duplicate data.
- Bound agent steps, tool calls, retries, and token usage when agentic behavior is introduced.
- Log useful diagnostic metadata without exposing sensitive payloads.

## Tests and validation

- Add or update tests when behavior changes.
- Add regression tests for bug fixes where practical.
- Test important failure cases as well as successful paths.
- Test observable behavior.
- Mock external service boundaries rather than the internal logic being tested.
- Default tests must be deterministic and runnable without credentials, internet access, paid APIs, or production services.
- Keep live integration tests explicitly opt-in.
- For changes to prompts, retrieval, model selection, tool routing, or agent behavior, run or update the relevant evaluation cases when such evaluation infrastructure exists.
- Mocked tests alone do not establish real model or retrieval quality.
- Run focused tests first, followed by broader checks justified by the affected area.
- Do not delete tests, weaken assertions, or disable checks merely to obtain a passing result.
- Explain intentional changes in expected behavior.

Use commands already configured by the repository.

Examples, only when the corresponding tools are configured:

```bash
uv sync --locked --python 3.12
uv run --locked python --version
uv run --locked pytest -q
uv run --locked ruff check src/ tests/
uv run --locked ruff format --check src/ tests/
git diff --check
```

If a required check cannot run, report the exact blocker.

Do not claim a check passed unless its result was actually observed.

## Git and existing work

- Check the current branch and `git status` before meaningful edits.
- Inspect relevant diffs before modifying existing work.
- Work on a feature branch.
- Respect a task-provided branch or worktree.
- When starting from the default branch, create a task branch before implementation.
- Preserve unrelated edits and staged changes.
- Do not overwrite, revert, or include unrelated work in a commit.
- Keep diffs focused.
- Avoid unrelated cleanup, broad formatting changes, generated artifacts, and large datasets.
- Review `git diff` before handoff.
- Review `git diff --cached` before committing.
- Stage only changes belonging to the current task.
- Commit, push, merge, publish, or deploy only when authorized by the current task.
- Do not discard work, rewrite shared history, force-push, or perform destructive data operations without explicit authorization.

## Completion report

At the end of a task, briefly state:

- What changed.
- Why it changed.
- Which checks were run.
- The outcome of those checks.
- Any checks not run.
- Remaining blockers, assumptions, risks, or limitations.

Explain important design choices in plain language so the repository remains useful as a learning artifact.

Never claim that a command, test, benchmark, commit, push, PR, merge, or deployment succeeded unless its result was actually observed.