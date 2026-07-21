# RepoPulse

Live AI project-intelligence pipeline: GitHub webhook → agent pipeline → live dashboard, with a Q&A agent grounded in current repo state.

See [CLAUDE.md](CLAUDE.md) for stack, conventions, and priorities, and [spec.md](spec.md) for the product spec.

This is currently a **scaffold**: routing, placeholder pages/components, shared data shapes, and empty backend/agent/infra modules. No feature logic, AI calls, or integrations are implemented yet.

## Structure

- `frontend/` — React + TypeScript + Tailwind dashboard
- `backend/` — FastAPI gateway, LangGraph pipeline, agents, Redis, RAG, services
- `docker/` — Dockerfiles (one per agent, plus backend/frontend)
- `kubernetes/` — deployment manifests (Minikube-oriented)
- `docs/` — additional documentation
- `scripts/` — dev/ops scripts
- `tests/` — cross-cutting/e2e tests

## Local development

```bash
cp .env.example .env
docker compose up
```

Backend: http://localhost:8000 · Frontend: http://localhost:5173
