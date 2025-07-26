export default function Input({ value, onChange, type = 'text', ...props }) {
  return (
    <input
      className="input"
      type={type}
      value={value}
      onChange={onChange}
      {...props}
    />
  );
}
