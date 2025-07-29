import { renderHook, waitFor } from '@testing-library/react';
import useFetch from '../../../frontend/src/hooks/useFetch';

describe('useFetch', () => {
  it('veri getirir', async () => {
    global.fetch = jest.fn().mockResolvedValue({
      json: () => Promise.resolve({ ok: true })
    }) as any;
    const { result } = renderHook(() => useFetch<{ok:boolean}>('/api'));
    await waitFor(() => expect(result.current.data).toEqual({ ok: true }));
  });
});
