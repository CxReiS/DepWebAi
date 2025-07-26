export default function Avatar({ src, alt }) {
  return <img src={src} alt={alt} style={{ width: 32, height: 32, borderRadius: '50%' }} />;
}
