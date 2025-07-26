// Basit global durum yöneticisi
import { createContext, useContext, useState } from 'react';

const StoreContext = createContext();

export function StoreProvider({ children }) {
  const [user, setUser] = useState(null);
  return (
    <StoreContext.Provider value={{ user, setUser }}>
      {children}
    </StoreContext.Provider>
  );
}

export const useStore = () => useContext(StoreContext);
