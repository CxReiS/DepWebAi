// Basit panel bileşeni
export default function Panel({ title, children }) {
  return (
    <section>
      <h3>{title}</h3>
      {children}
    </section>
  );
}
