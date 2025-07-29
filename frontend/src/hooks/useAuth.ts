// Giriş işlemleri için basit hook
import { useStore, User } from '../store/store';
import { login as apiLogin } from '../services';

export interface Credentials {
  username: string;
  password: string;
}

export default function useAuth() {
  const { user, setUser } = useStore();

  const login = async (credentials: Credentials) => {
    const data = await apiLogin(credentials);
    if (data.access_token) {
      const logged: User = {
        username: credentials.username,
        token: data.access_token,
      };
      setUser(logged);
    }
    return data;
  };

  return { user, login };
}
