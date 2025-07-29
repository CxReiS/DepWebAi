import { ReactNode, MouseEventHandler } from 'react';

type ButtonProps = {
  children: ReactNode;
  onClick?: MouseEventHandler<HTMLButtonElement>;
  type?: 'button' | 'submit' | 'reset';
  className?: string;
};

export default function Button({
  children,
  onClick,
  type = 'button',
  className,
}: ButtonProps) {
  return (
    <button type={type} onClick={onClick} className={className}>
      {children}
    </button>
  );
}
