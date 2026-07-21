import { createBrowserRouter } from "react-router-dom";
import MainLayout from "../layouts/MainLayout";
import Dashboard from "../pages/Dashboard";
import RepositoryConnect from "../pages/RepositoryConnect";
import RepositoryDetails from "../pages/RepositoryDetails";
import LiveActivity from "../pages/LiveActivity";
import PushHistory from "../pages/PushHistory";
import RiskAnalysis from "../pages/RiskAnalysis";
import TechnicalDebt from "../pages/TechnicalDebt";
import Documentation from "../pages/Documentation";
import AIChat from "../pages/AIChat";
import Settings from "../pages/Settings";
import Login from "../pages/Login";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <MainLayout />,
    children: [
      { index: true, element: <Dashboard /> },
      { path: "connect", element: <RepositoryConnect /> },
      { path: "repository/:id", element: <RepositoryDetails /> },
      { path: "activity", element: <LiveActivity /> },
      { path: "history", element: <PushHistory /> },
      { path: "risk", element: <RiskAnalysis /> },
      { path: "tech-debt", element: <TechnicalDebt /> },
      { path: "documentation", element: <Documentation /> },
      { path: "qa", element: <AIChat /> },
      { path: "settings", element: <Settings /> },
    ],
  },
  { path: "/login", element: <Login /> },
]);
