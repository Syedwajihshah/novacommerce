# NovaCommerce Environment Report

## Operating System
- Ubuntu 20.04.6 LTS

## Python
- System Python: 3.8.10
- NovaCommerce project Python: 3.12.15
- Environment manager: uv
- Project virtual environment: `.venv`

## Development Tools
- Git: 2.25.1
- GitHub CLI: 2.74.0
- VS Code: 1.141.0
- Codex CLI: 0.147.0
- Docker: 27.0.1
- Docker Compose: 2.28.1

## GPU
- NVIDIA GeForce RTX 2060
- VRAM: 6 GB
- NVIDIA driver: 545.29.06
- Driver CUDA compatibility: 12.3
- CUDA toolkit (`nvcc`): 11.8

## Environment Decisions
- Do not modify Ubuntu's system Python.
- Use Python 3.12 for NovaCommerce.
- Use `uv` for Python environment and dependency management.
- Keep project dependencies isolated inside `.venv`.
- Use the RTX 2060 selectively for embeddings, reranking, and feasible local-model experiments.