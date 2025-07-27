// Basit sekme çubuğu
export default function TabBar({ tabs, active, onChange }) {
  return (
    <div>
      {tabs.map(t => (
        <button key={t} onClick={() => onChange(t)} disabled={t === active}>
          {t}
        </button>
      ))}
    </div>
  );
}
