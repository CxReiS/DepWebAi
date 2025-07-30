import { render, screen } from '../test-utils';
import MainLayout from '../../../frontend/src/layouts/MainLayout';

test('MainLayout temel bolumleri gosterir', () => {
  render(
    <MainLayout>
      <p>İçerik</p>
    </MainLayout>
  );
  expect(screen.getByText('DeepWebAi')).toBeInTheDocument();
  expect(screen.getByText('Dashboard')).toBeInTheDocument();
  expect(screen.getByText('İçerik')).toBeInTheDocument();
});
