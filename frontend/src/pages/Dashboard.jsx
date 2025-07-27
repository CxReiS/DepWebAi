import { useEffect, useState } from 'react';
import { getUsers } from '../services/api';
import Panel from '../components/Panel';
import Widget from '../components/Widget';
import { useToast } from '../hooks/useToast.jsx';

export default function Dashboard() {
  const [users, setUsers] = useState([]);
  const { addToast } = useToast();
  useEffect(() => {
    getUsers()
      .then(setUsers)
      .catch(() => {
        setUsers([{ id: 1, username: 'demo' }]);
        addToast('Sunucu bağlantısı yok');
      });
  }, []);
  return (
    <div>
      <Widget title="Kullanıcılar">
        <Panel>
          {users.map((u) => (
            <div key={u.id}>{u.username}</div>
          ))}
        </Panel>
      </Widget>
    </div>
  );
}
