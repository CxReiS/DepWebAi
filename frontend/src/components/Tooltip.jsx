import { useState } from 'react';
export default function Tooltip({ text, children }) {
  const [show, setShow] = useState(false);
  return (
    <span onMouseEnter={() => setShow(true)} onMouseLeave={() => setShow(false)} style={{ position: 'relative' }}>
      {children}
      {show && (
        <span style={{ position: 'absolute', bottom: '100%', background: '#111', color: '#fff', padding: '2px 4px', borderRadius: 2 }}>
          {text}
        </span>
      )}
    </span>
  );
}
