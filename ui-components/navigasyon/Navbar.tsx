// Basit navbar bileşeni
export default function Navbar({ links }) {
  return (
    <nav>
      {links.map(l => (
        <a key={l.href} href={l.href}>{l.label}</a>
      ))}
    </nav>
  );
}
