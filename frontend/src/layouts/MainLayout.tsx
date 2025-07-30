import Navbar from '../components/Navbar';
import Sidebar from '../components/Sidebar';
import { ThemeProvider } from '../hooks/useTheme';
import { ToastProvider } from '../hooks/useToast';
import type { LayoutProps } from './LayoutProps';
export default function MainLayout({ children }: LayoutProps) {
  return (
    <ThemeProvider>
      <ToastProvider>
        <Navbar />
        <div className="main">
          <Sidebar />
          <div className="content">{children}</div>
        </div>
      </ToastProvider>
    </ThemeProvider>
  );
}
