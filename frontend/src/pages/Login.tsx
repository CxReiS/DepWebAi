import { useState } from 'react';
import { login } from '../services';
import Input from '../components/Input';
import Button from '../components/Button';
import { useToast } from '../hooks/useToast';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { addToast } = useToast();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await login({ username, password });
    if (data.access_token) {
      localStorage.setItem('token', data.access_token);
      addToast('Giriş başarılı');
    } else {
      addToast('Giriş başarısız');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Kullanıcı" />
      <Input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Parola" />
      <Button type="submit">Giriş</Button>
    </form>
  );
}
