import { render, screen } from '../test-utils';
import Navbar from '../../../frontend/src/components/Navbar';

test('navbar baslik gosterilir', () => {
  render(<Navbar />);
  expect(screen.getByText('DeepWebAi')).toBeInTheDocument();
});
