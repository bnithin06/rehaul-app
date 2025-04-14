'use client'

import { createContext, useState, useEffect } from 'react'
import { jwtDecode } from 'jwt-decode'
import { useRouter } from 'next/navigation'

const AuthContext = createContext()

export default AuthContext

export const AuthProvider = ({ children }) => {
  const router = useRouter()

  const [authTokens, setAuthTokens] = useState(null)
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)

  // Load tokens and user from localStorage (client-side only)
  useEffect(() => {
    const tokens = localStorage.getItem('authTokens')
    if (tokens) {
      const parsedTokens = JSON.parse(tokens)
      setAuthTokens(parsedTokens)
      setUser(jwtDecode(parsedTokens.access))
    }
    setLoading(false)
  }, [])

  const loginUser = async (e) => {
    e.preventDefault()
    setError(false)

    try {
      const response = await fetch('http://localhost:8000/auth/token/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
        //   phone_number: e.target.phone_number.value,
        //   password: e.target.password.value,

          phone_number: "9908169058",
          password:"1234",
        }),
      })

      const data = await response.json()

      if (response.status === 200) {
        const decoded = jwtDecode(data.access)
        const tokens = { access: data.access, refresh: data.refresh }

        setAuthTokens(tokens)
        setUser(decoded)
        localStorage.setItem('authTokens', JSON.stringify(tokens))
        routeBasedOnRole(decoded.role)
      } else {
        setError(true)
      }
    } catch (err) {
      console.error('Login error:', err)
      setError(true)
    }
  }

  const logoutUser = () => {
    setAuthTokens(null)
    setUser(null)
    localStorage.removeItem('authTokens')
    router.push('/')
  }

  const updateToken = async () => {
    const storedTokens = localStorage.getItem('authTokens')
    const refreshToken = storedTokens ? JSON.parse(storedTokens).refresh : null

    if (!refreshToken) {
      logoutUser()
      return
    }

    try {
      const response = await fetch('http://localhost:8000/auth/token/refresh/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh: refreshToken }),
      })

      const data = await response.json()

      if (response.status === 200) {
        const updatedTokens = {
          access: data.access,
          refresh: refreshToken,
        }

        setAuthTokens(updatedTokens)
        const decoded = jwtDecode(data.access)
        setUser(decoded)
        localStorage.setItem('authTokens', JSON.stringify(updatedTokens))
      } else {
        logoutUser()
      }
    } catch (err) {
      console.error('Token refresh error:', err)
      logoutUser()
    }
  }

  const routeBasedOnRole = (role) => {
    switch (role) {
      case 'driver':
        router.push('/dashboard/driver')
        break
      case 'lorry_owner':
        router.push('/dashboard/lorry-owner')
        break
      case 'business':
        router.push('/dashboard/merchant')
        break
      case 'admin':
        router.push('/dashboard/admin')
        break
      default:
        router.push('/')
    }
  }

  // Auto-refresh token every 4 minutes
  useEffect(() => {
    if (!authTokens) return

    const interval = setInterval(() => {
      updateToken()
    }, 1000 * 60 * 4)

    return () => clearInterval(interval)
  }, [authTokens])

  const contextData = {
    user,
    authTokens,
    loginUser,
    logoutUser,
    error,
  }

  return (
    <AuthContext.Provider value={contextData}>
      {loading ? null : children}
    </AuthContext.Provider>
  )
}