import { render, screen } from '../test-utils';
import AuthLayout from '../../../frontend/src/layouts/AuthLayout';

test('AuthLayout sadece icerigi gosterir', () => {
  render(
    <AuthLayout>
      <p>Giris Sayfasi</p>
    </AuthLayout>
  );
  expect(screen.getByText('Giris Sayfasi')).toBeInTheDocument();
  expect(screen.queryByText('DeepWebAi')).toBeNull();
});
