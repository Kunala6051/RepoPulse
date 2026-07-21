import { NavLink } from "react-router-dom";

const links = [
  { to: "/", label: "Dashboard" },
  { to: "/connect", label: "Repository Connect" },
  { to: "/activity", label: "Live Activity" },
  { to: "/history", label: "Push History" },
  { to: "/risk", label: "Risk Analysis" },
  { to: "/tech-debt", label: "Technical Debt" },
  { to: "/documentation", label: "Documentation" },
  { to: "/qa", label: "AI Chat" },
  { to: "/settings", label: "Settings" },
];

export default function Sidebar() {
  return (
    <aside className="w-56 border-r border-gray-200 p-4">
      <nav className="flex flex-col gap-1">
        {links.map((link) => (
          <NavLink
            key={link.to}
            to={link.to}
            className={({ isActive }) =>
              `rounded px-3 py-2 text-sm ${isActive ? "bg-gray-100 font-semibold" : "text-gray-600"}`
            }
          >
            {link.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
