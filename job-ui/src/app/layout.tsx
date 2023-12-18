import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import Header from './components/Header'
import Container from './components/Container'
import Footer from './components/Footer'


const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Programmer job app',
  description: 'Application for viewing job listings with certain programming languages as requirements',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      
      <body className={inter.className}>
        <Container>
          <Header/>
          {children}
          <Footer/>
        </Container>
        </body>
    </html>
  )
}
