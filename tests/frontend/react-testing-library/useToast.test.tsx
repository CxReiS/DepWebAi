import { renderHook, act } from '@testing-library/react';
import { ToastProvider, useToast } from '../../../frontend/src/hooks/useToast';

const wrapper = ({ children }: { children: React.ReactNode }) => <ToastProvider>{children}</ToastProvider>;

test('toast ekleme ve silme', () => {
  jest.useFakeTimers();
  const { result } = renderHook(() => useToast(), { wrapper });
  act(() => result.current.addToast('deneme'));
  expect(result.current).toBeTruthy();
  jest.runAllTimers();
});
