# Project

RepoPulse is a live AI project-intelligence pipeline that connects to a GitHub repo via webhook, runs every push through specialized AI agents (Documentation, Risk, Tech Debt, Summary, Q&A), and updates a live dashboard in real time — letting a non-technical PM ask plain-language questions grounded in the actual repo state.

Stack:
- Frontend: React + WebSocket (live dashboard)
- Backend gateway: FastAPI (receives GitHub webhooks)
- Agent orchestration: LangGraph (Python)
- Queue / shared state: Redis (event stream between gateway and agents, cache for repo metadata + embeddings)
- Containers: Docker (one image per agent)
- Orchestration: Kubernetes (Minikube locally) — one worker pod per agent, scales with push volume
- DB (if used): PostgreSQL (tech-debt history over time)
- LLM: Claude, via Anthropic API

# Conventions

- Python: type hints required, format with `black`, lint with `ruff`.
- JavaScript/React: functional components only, no class components. Tailwind for styling. Components in `src/components/`, pages in `src/pages/`.
- Keep each agent as a self-contained module under `agents/<agent_name>/` — no shared mutable state between agents except through Redis.
- No `any` / untyped dicts for data passed between the gateway and agents — define a shared schema (Pydantic models) for webhook payloads and agent outputs.
- Config (Redis URL, Claude API key, GitHub webhook secret) via environment variables only — never hardcoded.

# Testing

- Run backend tests: `pytest tests/`
- Run frontend tests: `npm test`
- Every new agent gets at least one integration test that mocks a GitHub push payload and asserts the agent produces valid structured output.
- Before marking any Must-have feature "done," it needs a passing end-to-end test: webhook in → dashboard update out.

# Git workflow

- Branch per feature: `feature/<agent-name>` or `feature/<component>`.
- Commit messages: `feat: ...`, `fix: ...`, `refactor: ...`, `chore: ...`.
- Never push directly to `main`. Open a PR, at least one teammate reviews before merge.
- Keep commits small and scoped to one agent/component at a time — this project's own demo depends on clean, individually meaningful commits, so practice what we're building.

# Boundaries

- Do not delete files without asking first.
- Do not modify `.env` or any secrets file.
- Do not install new packages without confirming — check `requirements.txt` / `package.json` first, and ask before adding a new dependency.
- Do not touch Kubernetes manifests or Dockerfiles without flagging the change, since these affect the live demo environment directly.
- Never fabricate agent output when a real API call fails — surface the error instead of silently faking a result. This project's whole pitch depends on being honestly grounded; the code should reflect that.

# Priorities (MoSCoW)

**Must (build first, in this order):**
1. Webhook → Redis → pipeline → dashboard update, end to end, no manual refresh.
2. Q&A agent answering a real question grounded in current repo state.
3. At least one more agent (Risk or Summary) visibly producing real output.

**Should (after Musts work):**
- Second/third agent fully working.
- Visible Kubernetes pod scaling (simplified queue-watcher version, not full HPA).

**Could (cut without guilt if time runs short):**
- Full historical tech-debt trend tracking in Postgres.
- SonarQube API integration for tech-debt scoring.
- Multi-repo support, auth/roles, Ansible-automated deploy.

# Why this matters

Without this file, every Claude Code session starts from zero and has to re-guess the stack, conventions, and priorities. With it, Claude already knows this is a Redis + Kubernetes + Docker + LangGraph project, what's a Must vs. a Could, and where the actual boundaries are — so prompts can be short and Claude won't suggest rebuilding SonarQube from scratch or wiring up features that aren't in scope for the week.