import { ThemeProvider } from '../hooks/useTheme';
import { ToastProvider } from '../hooks/useToast';
import type { LayoutProps } from './LayoutProps';

export default function AuthLayout({ children }: LayoutProps) {
  return (
    <ThemeProvider>
      <ToastProvider>
        <div className="auth-layout">{children}</div>
      </ToastProvider>
    </ThemeProvider>
  );
}
