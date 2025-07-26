// Basit kart bileşeni
export default function Card({ title, content }) {
  return (
    <div className="card">
      <h4>{title}</h4>
      <div>{content}</div>
    </div>
  );
}
