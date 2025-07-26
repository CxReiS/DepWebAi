// Giriş işlemleri için basit hook
import { useStore } from '../store/store';
import { login as apiLogin } from '../services/api';

export default function useAuth() {
  const { user, setUser } = useStore();

  const login = async (credentials) => {
    const data = await apiLogin(credentials);
    if (data.access_token) {
      setUser({ username: credentials.username, token: data.access_token });
    }
    return data;
  };

  return { user, login };
}
