export interface LayoutProps {
  children: React.ReactNode;
}

export type Layout = (props: LayoutProps) => JSX.Element | null;
