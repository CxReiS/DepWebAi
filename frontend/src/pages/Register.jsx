import { useState } from 'react';
import Input from '../components/Input';
import Button from '../components/Button';
import { useToast } from '../hooks/useToast.jsx';
import { register } from '../services/api';

export default function Register() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const { addToast } = useToast();

  const handleSubmit = async (e) => {
    e.preventDefault();
    await register({ username, email, password });
    addToast('Kayıt oluşturuldu');
    setUsername('');
    setEmail('');
    setPassword('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Kullanıcı" />
      <Input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
      <Input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Parola" />
      <Button type="submit">Kayıt Ol</Button>
    </form>
  );
}
