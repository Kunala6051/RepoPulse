from fastapi import FastAPI

from backend.api.routes import activity, chat, dashboard, repositories, risk, summary, tech_debt, webhook

app = FastAPI(title="RepoPulse API")

app.include_router(webhook.router)
app.include_router(repositories.router)
app.include_router(dashboard.router)
app.include_router(risk.router)
app.include_router(tech_debt.router)
app.include_router(chat.router)
app.include_router(activity.router)
app.include_router(summary.router)
