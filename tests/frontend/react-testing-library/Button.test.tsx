import { render, fireEvent, screen } from '../test-utils';
import Button from '../../../frontend/src/components/Button';

test('buton tiklaninca callback calisir', () => {
  const onClick = jest.fn();
  render(<Button onClick={onClick}>Tıkla</Button>);
  fireEvent.click(screen.getByRole('button'));
  expect(onClick).toHaveBeenCalled();
});

test('variant sinifi uygulanir', () => {
  render(<Button variant="secondary">Test</Button>);
  const btn = screen.getByRole('button');
  expect(btn.className).toContain('button-secondary');
});
