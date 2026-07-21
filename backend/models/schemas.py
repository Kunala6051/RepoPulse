from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class AgentName(str, Enum):
    DOCUMENTATION = "documentation"
    RISK = "risk"
    TECH_DEBT = "tech_debt"
    SUMMARY = "summary"
    QA = "qa"


class AgentStatus(str, Enum):
    IDLE = "idle"
    RUNNING = "running"
    DONE = "done"
    ERROR = "error"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Repository(BaseModel):
    id: str
    name: str
    owner: str
    branch: str


class Commit(BaseModel):
    id: str
    hash: str
    author: str
    message: str
    timestamp: datetime


class WebhookEvent(BaseModel):
    id: str
    repository: Repository
    commits: list[Commit]
    received_at: datetime


class AgentResult(BaseModel):
    agent: AgentName
    push_id: str
    status: AgentStatus
    output: str


class RiskFlag(BaseModel):
    file: str
    severity: Severity
    reason: str
    affected_modules: list[str]


class RiskReport(BaseModel):
    score: float
    affected_modules: list[str]
    severity: Severity
    flags: list[RiskFlag]


class TechDebtItem(BaseModel):
    file: str
    description: str
    severity: Severity


class TechDebtReport(BaseModel):
    score: float
    items: list[TechDebtItem]


class DocumentationSummary(BaseModel):
    file: str
    summary: str


class QAMessage(BaseModel):
    id: str
    role: str
    text: str
    grounded_in: list[str]
    timestamp: datetime


class RepoConnection(BaseModel):
    id: str
    owner: str
    name: str
    branch: str
    webhook_status: str


class Notification(BaseModel):
    id: str
    message: str
    level: str
    timestamp: datetime
    read: bool
