// Backend istekleri için basit fonksiyonlar

export async function login(credentials) {
  const res = await fetch('/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(credentials)
  });
  return res.json();
}

export async function getUsers() {
  const res = await fetch('/users/');
  return res.json();
}
