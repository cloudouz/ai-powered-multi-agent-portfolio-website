import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'AI Portfolio Agents',
  description: 'AI-Powered Multi-Agent Portfolio Website',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
