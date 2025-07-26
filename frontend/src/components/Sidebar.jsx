import { Link } from 'react-router-dom';
export default function Sidebar() {
  const links = [
    { to: '/', label: 'Dashboard' },
    { to: '/login', label: 'Giriş' },
    { to: '/register', label: 'Kayıt' },
  ];
  return (
    <div className="sidebar">
      {links.map((l) => (
        <div key={l.to}>
          <Link to={l.to}>{l.label}</Link>
        </div>
      ))}
    </div>
  );
}
