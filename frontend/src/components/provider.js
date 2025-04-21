'use client'

import { AuthProvider } from "@/context/AuthContext"
import Navbar from "./navbar/Navbar"
import Footer from "./footer/footer"

export default function Providers({ children }) {
  return (
    <AuthProvider>
      <>
        <Navbar />
        {children}
        <Footer/>
      </>
    </AuthProvider>
  )
}