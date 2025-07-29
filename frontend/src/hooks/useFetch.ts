import { useEffect, useState } from 'react';

export default function useFetch<T = unknown>(url: string, options?: RequestInit) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    if (!url) return;
    let ignore = false;
    const fetchData = async () => {
      setLoading(true);
      try {
        const res = await fetch(url, options);
        const json = (await res.json()) as T;
        if (!ignore) setData(json);
      } catch (err) {
        if (!ignore) setError(err as Error);
      } finally {
        if (!ignore) setLoading(false);
      }
    };
    fetchData();
    return () => {
      ignore = true;
    };
  }, [url]);

  return { data, loading, error };
}
