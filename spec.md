# RepoPulse — Spec

*A scaffold is a living spec. This file is the reference — update it as the build evolves.*

## What it is

RepoPulse is a live AI project-intelligence pipeline. It connects to a team's GitHub repo via webhook; every push runs through a set of specialized AI agents (Documentation, Risk, Tech Debt, Summary) that analyze the change, and results appear on a live dashboard in real time. A project manager can also ask plain-language questions ("which files are riskiest to touch right now") and get answers grounded in the actual repo state via a Q&A agent.

## Problem

On any codebase of real size, a PM can't read every file. Getting basic answers — what changed, what's risky, what's falling behind — means interrupting a developer. It's slow and inconsistent. RepoPulse gives a PM independent, live visibility without needing to ask.

## Pages / Routes

| Route | Page | Status |
|---|---|---|
| `/` | Dashboard — live agent pipeline, activity log, Q&A input | **Built** (demo screen) |
| `/qa` | Full Q&A history/thread view | Placeholder |
| `/history` | Past pushes + agent runs log | Placeholder |
| `/connect` | Connect a GitHub repo, manage webhook | Placeholder |

## Data shapes (`src/types.ts`)

- `PushEvent` — a single commit push: sha, author, message, files changed, list of `AgentRun`s
- `AgentRun` — one agent's execution against a push: agent name, status (idle/running/done/error), output text
- `RiskFlag` — a flagged file: severity, reason, downstream modules affected
- `QAMessage` — one turn in the Q&A thread: role, text, what it's grounded in
- `RepoConnection` — the connected repo: owner, name, webhook status

These are defined before wiring any real API — every screen is typed against them.

## Tech stack

- **Frontend:** React + TypeScript + Tailwind, React Router
- **Backend gateway:** FastAPI (receives GitHub webhooks)
- **Agent orchestration:** LangGraph (Python), Claude for reasoning
- **Queue / shared state:** Redis — event stream between gateway and agents, cache for repo metadata
- **Containers:** Docker — one image per agent
- **Orchestration:** Kubernetes (Minikube locally) — one worker pod per agent
- **DB (optional, for tech-debt history):** PostgreSQL

## Priorities (MoSCoW)

**Must**
1. Webhook → Redis → agent pipeline → dashboard update, live, no manual refresh
2. Q&A agent answering a real question grounded in current repo state
3. At least one more agent (Risk or Summary) visibly producing real output

**Should**
- Second/third agent fully working end to end
- Visible Kubernetes pod scaling (simplified queue-watcher, not full HPA)

**Could**
- Full historical tech-debt trend tracking in Postgres
- SonarQube API integration for tech-debt scoring
- Multi-repo support, auth/roles, Ansible-automated deploy

## What makes this different from existing tools

SonarQube scans code for a developer. RepoPulse translates a change into plain language for a PM and answers open-ended questions grounded in live repo state — a different layer, not a competing scanner. Where possible, integrate with SonarQube's API for tech-debt scoring rather than rebuilding it.

## Demo script

1. Push a real commit live.
2. Watch the four agent nodes light up in sequence on the Dashboard.
3. Watch the activity log fill in per-agent, no manual refresh.
4. Ask a live question in the Q&A box tied to that exact change.
5. Get a grounded answer back.

## Current state

Scaffold complete: routing, placeholder pages, data shapes, and one fully working screen (Dashboard, running on mock data). Next: replace `src/lib/mockPipeline.ts` with real calls to the FastAPI backend once the webhook → Redis → agents pipeline exists.