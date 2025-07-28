export const Link = ({ to, children }: { to: string; children: React.ReactNode }) => (
  <a href={to}>{children}</a>
);
