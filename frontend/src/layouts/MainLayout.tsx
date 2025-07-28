import Navbar from '../components/Navbar';
import Sidebar from '../components/Sidebar';
import { ThemeProvider } from '../hooks/useTheme';
import { ToastProvider } from '../hooks/useToast';
import { StoreProvider } from '../store/store';

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
