// Basit toast bildirimi yonetimi
import { createContext, useState, type ReactNode, useMemo, useCallback } from 'react';
interface Toast {
  id: number;
  message: string;
}

interface ToastContextValue {
  addToast: (message: string) => void;
}

const ToastContext = createContext<ToastContextValue | undefined>(undefined);

export function ToastProvider({ children }: { readonly children: ReactNode }) {
  const [items, setItems] = useState<Toast[]>([]);

  const removeToast = (id: number) => {
    setItems((v) => v.filter((t) => t.id !== id));
  };

  const addToast = useCallback((message: string) => {
    const id = Date.now();
    setItems((v) => [...v, { id, message }]);
    setTimeout(() => removeToast(id), 3000);
  }, []);

  const contextValue = useMemo(() => ({ addToast }), [addToast]);

  return (
    <ToastContext.Provider value={contextValue}>
      {children}
      <div className="toast-container">
        {items.map((t) => (
          <div key={t.id} className="toast">{t.message}</div>
        ))}
      </div>
    </ToastContext.Provider>
  );
}

// Remove useToast export from this file and move it to useToastHook.ts
