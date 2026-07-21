export type AgentName = "documentation" | "risk" | "tech_debt" | "summary" | "qa";

export type AgentStatus = "idle" | "running" | "done" | "error";

export interface AgentRun {
  agent: AgentName;
  status: AgentStatus;
  output: string;
  startedAt: string;
  finishedAt?: string;
}

export interface PushEvent {
  id: string;
  sha: string;
  author: string;
  message: string;
  filesChanged: string[];
  timestamp: string;
  agentRuns: AgentRun[];
}

export interface RiskFlag {
  file: string;
  severity: "low" | "medium" | "high";
  reason: string;
  affectedModules: string[];
}

export interface RiskReport {
  score: number;
  affectedModules: string[];
  severity: "low" | "medium" | "high";
  flags: RiskFlag[];
}

export interface TechDebtItem {
  file: string;
  description: string;
  severity: "low" | "medium" | "high";
}

export interface TechDebtReport {
  score: number;
  items: TechDebtItem[];
}

export interface DocumentationSummary {
  file: string;
  summary: string;
}

export interface QAMessage {
  id: string;
  role: "user" | "assistant";
  text: string;
  groundedIn: string[];
  timestamp: string;
}

export interface RepoConnection {
  id: string;
  owner: string;
  name: string;
  branch: string;
  webhookStatus: "connected" | "disconnected" | "pending";
}

export interface Repository {
  id: string;
  name: string;
  owner: string;
  branch: string;
}

export interface Commit {
  id: string;
  hash: string;
  author: string;
  message: string;
  timestamp: string;
}

export interface AgentResult {
  agent: AgentName;
  pushId: string;
  status: AgentStatus;
  output: string;
}

export interface WebhookEvent {
  id: string;
  repository: Repository;
  commits: Commit[];
  receivedAt: string;
}

export interface User {
  id: string;
  name: string;
  email: string;
  role: "pm" | "developer" | "admin";
}

export interface Notification {
  id: string;
  message: string;
  level: "info" | "warning" | "error";
  timestamp: string;
  read: boolean;
}
