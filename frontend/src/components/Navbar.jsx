import { Link } from 'react-router-dom';
import { useTheme } from '../hooks/useTheme.jsx';
import Avatar from './Avatar';

export default function Navbar() {
  const { theme, setTheme } = useTheme();
  const toggle = () => setTheme(theme === 'light' ? 'dark' : 'light');
  return (
    <div className="navbar">
      <Link to="/">DeepWebAi</Link>
      <Link to="/login">Giriş</Link>
      <Link to="/register">Kayıt</Link>
      <button onClick={toggle} className="button">{theme === 'light' ? '🌞' : '🌙'}</button>
      <Avatar src="https://via.placeholder.com/32" alt="user" />
    </div>
  );
}
