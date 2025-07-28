import { render, fireEvent, screen, act } from '../test-utils';
import { ToastProvider, useToast } from '../../../frontend/src/hooks/useToast';

function Demo() {
  const { addToast } = useToast();
  return <button onClick={() => addToast('Merhaba')}>Ekle</button>;
}

test('toast eklenip otomatik silinir', () => {
  jest.useFakeTimers();
  render(
    <ToastProvider>
      <Demo />
    </ToastProvider>
  );
  fireEvent.click(screen.getByText('Ekle'));
  expect(screen.getByText('Merhaba')).toBeInTheDocument();
  act(() => {
    jest.runAllTimers();
  });
  expect(screen.queryByText('Merhaba')).not.toBeInTheDocument();
  jest.useRealTimers();
});
