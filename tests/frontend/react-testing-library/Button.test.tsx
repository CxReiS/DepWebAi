import { render, screen, fireEvent } from '@testing-library/react';
import Button from '../../../frontend/src/components/Button';

test('butona tiklandiginda callback calisir', () => {
  const handler = jest.fn();
  render(<Button onClick={handler}>Kaydet</Button>);
  fireEvent.click(screen.getByRole('button'));
  expect(handler).toBeCalled();
});
