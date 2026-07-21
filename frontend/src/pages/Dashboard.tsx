import RecentPushesCard from "../components/dashboard/RecentPushesCard";
import RepositoryHealthCard from "../components/dashboard/RepositoryHealthCard";
import RiskSummaryCard from "../components/dashboard/RiskSummaryCard";
import TechnicalDebtCard from "../components/dashboard/TechnicalDebtCard";
import AgentStatusCard from "../components/dashboard/AgentStatusCard";
import ActivityTimeline from "../components/dashboard/ActivityTimeline";

export default function Dashboard() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      <p className="text-sm text-gray-500">Live agent pipeline, activity log, and repo health at a glance.</p>
      <div className="mt-6 grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
        <RecentPushesCard />
        <RepositoryHealthCard />
        <RiskSummaryCard />
        <TechnicalDebtCard />
        <AgentStatusCard />
        <ActivityTimeline />
      </div>
    </div>
  );
}
