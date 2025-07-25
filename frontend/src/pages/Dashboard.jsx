// Dashboard sayfası
import { useEffect, useState } from 'react';
import { getUsers } from '../services/api';

export default function Dashboard() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    getUsers().then(setUsers);
  }, []);

  return (
    <ul>
      {users.map(u => (<li key={u.id}>{u.username}</li>))}
    </ul>
  );
}
