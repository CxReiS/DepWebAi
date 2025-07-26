export default function Checkbox({ checked, onChange }) {
  return (
    <label>
      <input
        type="checkbox"
        className="checkbox"
        checked={checked}
        onChange={(e) => onChange(e.target.checked)}
      />
    </label>
  );
}
