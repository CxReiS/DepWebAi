// Giriş sayfası örneği
import { useState } from 'react';
import { login } from '../services/api';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await login({ username, password });
    localStorage.setItem('token', data.access_token);
    setMessage(data.message);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={username} onChange={e => setUsername(e.target.value)} />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
      <button type="submit">Giriş</button>
      {message && <div>{message}</div>}
    </form>
  );
}
