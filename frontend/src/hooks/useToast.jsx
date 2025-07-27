// Basit toast bildirimi yonetimi
import { createContext, useContext, useState } from 'react';

const ToastContext = createContext();

export function ToastProvider({ children }) {
  const [items, setItems] = useState([]);

  const addToast = (message) => {
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

export const useToast = () => useContext(ToastContext);
