import { renderHook, act } from '@testing-library/react';
import { ThemeProvider, useTheme } from '../../../frontend/src/hooks/useTheme';

describe('useTheme', () => {
  it('varsayilan deger light', () => {
    const { result } = renderHook(() => useTheme(), { wrapper: ThemeProvider });
    expect(result.current.theme).toBe('light');
    act(() => result.current.setTheme('dark'));
    expect(result.current.theme).toBe('dark');
  });
});
