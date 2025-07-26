// Basit modal bileşeni
export default function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null;
  return (
    <div className="modal">
      <button onClick={onClose}>Kapat</button>
      {children}
    </div>
  );
}
