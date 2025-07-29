// Basit toast bildirimi yonetimi
import { createContext, useContext, useState, ReactNode } from 'react';

type Toast = { id: number; message: string };
type ToastContextType = { addToast: (message: string) => void };

const ToastContext = createContext<ToastContextType | undefined>(undefined);

export function ToastProvider({ children }: { children: ReactNode }) {
  const [items, setItems] = useState<Toast[]>([]);

  const addToast = (message: string) => {
    const id = Date.now();
    setItems((v) => [...v, { id, message }]);
    setTimeout(() => setItems((v) => v.filter((t) => t.id !== id)), 3000);
  };

  return (
    <ToastContext.Provider value={{ addToast }}>
      {children}
      <div className="toast-container">
        {items.map((t) => (
          <div key={t.id} className="toast">{t.message}</div>
        ))}
      </div>
    </ToastContext.Provider>
  );
}

export const useToast = (): ToastContextType => {
  const ctx = useContext(ToastContext);
  if (!ctx) throw new Error('ToastProvider missing');
  return ctx;
};
