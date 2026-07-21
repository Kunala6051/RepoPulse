import { createContext, useContext } from "react";
import type { User, RepoConnection } from "../types";

interface AppContextValue {
  user: User | null;
  activeRepository: RepoConnection | null;
}

const AppContext = createContext<AppContextValue>({
  user: null,
  activeRepository: null,
});

export function useAppContext() {
  return useContext(AppContext);
}

export function AppProvider({ children }: { children: React.ReactNode }) {
  const value: AppContextValue = { user: null, activeRepository: null };
  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}
