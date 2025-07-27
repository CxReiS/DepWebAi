import Navbar from '../components/Navbar';
import Sidebar from '../components/Sidebar';
import { ThemeProvider } from '../hooks/useTheme.jsx';
import { ToastProvider } from '../hooks/useToast.jsx';
import { StoreProvider } from '../store/store.jsx';

export default function MainLayout({ children }) {
  return (
    <ThemeProvider>
      <ToastProvider>
        <StoreProvider>
          <Navbar />
          <div className="main">
            <Sidebar />
            <div className="content">{children}</div>
          </div>
        </StoreProvider>
      </ToastProvider>
    </ThemeProvider>
  );
}
