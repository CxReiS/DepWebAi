import { forwardRef, type ButtonHTMLAttributes } from 'react';

export type ButtonVariant = 'primary' | 'secondary';

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
}

const variantClass: Record<ButtonVariant, string> = {
  primary: 'button',
  secondary: 'button button-secondary',
};

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', className = '', ...rest }, ref) => {
    const cls = `${variantClass[variant]} ${className}`.trim();
    return <button ref={ref} className={cls} {...rest} />;
  }
);

Button.displayName = 'Button';

export default Button;
