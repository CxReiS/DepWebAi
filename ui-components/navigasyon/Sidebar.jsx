// Basit kenar çubuğu
export default function Sidebar({ items }) {
  return (
    <aside>
      <ul>
        {items.map(i => (
          <li key={i}>{i}</li>
        ))}
      </ul>
    </aside>
  );
}
