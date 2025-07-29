import { render, screen } from '../test-utils';
import Navbar from '../../../frontend/src/components/Navbar';
import { ThemeProvider } from '../../../frontend/src/hooks/useTheme';

test('navbar baslik gosterilir', () => {
  render(
    <ThemeProvider>
      <Navbar />
    </ThemeProvider>
  );
  expect(screen.getByText('DeepWebAi')).toBeInTheDocument();
});
