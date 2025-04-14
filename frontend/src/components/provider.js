'use client'

import { AuthProvider } from "@/context/AuthContext"
import Navbar from "./navbar/Navbar"

export default function Providers({ children }) {
  return (
    <AuthProvider>
      <>
        <Navbar />
        {children}
      </>
    </AuthProvider>
  )
}