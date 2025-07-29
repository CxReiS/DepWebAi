// Küçük global state örneği
import { create } from 'zustand';

export interface User {
  username: string;
  token: string;
}

interface Store {
  user: User | null;
  setUser: (user: User | null) => void;
}

export const useStore = create<Store>((set) => ({
  user: null,
  setUser: (user) => set({ user })
}));
