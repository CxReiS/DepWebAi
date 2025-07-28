import { render, fireEvent, screen } from '../test-utils';
import Button from '../../../frontend/src/components/Button';

test('buton tiklaninca callback calisir', () => {
  const onClick = jest.fn();
  render(<Button onClick={onClick}>Tıkla</Button>);
  fireEvent.click(screen.getByRole('button'));
  expect(onClick).toHaveBeenCalled();
});
