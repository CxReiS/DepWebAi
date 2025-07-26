// Basit navbar bileşeni
import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav>
      <Link to="/">Anasayfa</Link> | <Link to="/login">Giriş</Link>
    </nav>
  );
}
