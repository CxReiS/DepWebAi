import { renderHook, act } from '@testing-library/react';
import useAuth, { Credentials } from '../../../frontend/src/hooks/useAuth';

jest.mock('../../../frontend/src/services', () => ({
  login: jest.fn()
}));
import * as services from '../../../frontend/src/services';

jest.mock('../../../frontend/src/store/store', () => {
  const state: any = { user: null, setUser: (u: any) => (state.user = u) };
  const useStore = Object.assign(() => state, { getState: () => state });
  return { useStore };
});
import { useStore } from '../../../frontend/src/store/store';

describe('useAuth', () => {
  it('login basarili', async () => {
    const mockLogin = jest.spyOn(services, 'login').mockResolvedValue({ access_token: 'abc' });
    const { result } = renderHook(() => useAuth());
    await act(async () => {
      await result.current.login({ username: 'u', password: 'p' } as Credentials);
    });
    expect(useStore.getState().user?.token).toBe('abc');
    mockLogin.mockRestore();
  });
});
