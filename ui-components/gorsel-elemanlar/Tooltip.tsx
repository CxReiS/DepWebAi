// Basit bilgi balonu
export default function Tooltip({ text, children }) {
  return (
    <span className="tooltip" title={text}>
      {children}
    </span>
  );
}
