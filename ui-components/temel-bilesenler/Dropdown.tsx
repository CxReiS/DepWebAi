// Basit dropdown bileşeni
export default function Dropdown({ options, onSelect }) {
  return (
    <select onChange={e => onSelect(e.target.value)}>
      {options.map(opt => (
        <option key={opt} value={opt}>{opt}</option>
      ))}
    </select>
  );
}
