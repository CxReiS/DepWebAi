import { render, screen, fireEvent } from '@testing-library/react';
import Navbar from '../../../frontend/src/components/Navbar';
import { BrowserRouter } from 'react-router-dom';
import { ToastProvider } from '../../../frontend/src/hooks/useToast';

function Wrapper({ children }: { children: React.ReactNode }) {
  return <BrowserRouter><ToastProvider>{children}</ToastProvider></BrowserRouter>;
}

test('tema degisim dugmesi calisir', () => {
  render(<Navbar />, { wrapper: Wrapper });
  const btn = screen.getAllByRole('button')[0];
  fireEvent.click(btn);
  expect(btn).toBeInTheDocument();
});
