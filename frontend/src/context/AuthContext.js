'use client'

import { createContext, useState, useEffect, useCallback, useMemo } from 'react'
import { jwtDecode } from 'jwt-decode'
import { useRouter } from 'next/navigation'
import axios from 'axios'

const AuthContext = createContext(null)

export default AuthContext

const REFRESH_INTERVAL_MS = 1000 * 60 * 4

export const AuthProvider = ({ children }) => {
  const router = useRouter()
  const [authTokens, setAuthTokens] = useState(null)
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const routeBasedOnRole = useCallback((role) => {
    const routes = {
      driver: '/dashboard/driver',
      lorry_owner: '/dashboard/lorry-owner',
      business: '/dashboard/merchant',
      admin: '/dashboard/admin'
    }
    router.push(routes[role] || '/')
  }, [router])

  useEffect(() => {
    const loadAuthData = () => {
      try {
        const tokens = localStorage.getItem('authTokens')
        if (tokens) {
          const parsedTokens = JSON.parse(tokens)
          const decodedUser = jwtDecode(parsedTokens.access)

          setAuthTokens(parsedTokens)
          setUser(decodedUser)

          if (Date.now() >= decodedUser.exp * 1000) {
            logoutUser()
          }
        }
      } catch (err) {
        console.error('Failed to load auth data:', err)
        logoutUser()
      } finally {
        setLoading(false)
      }
    }

    loadAuthData()
  }, [])

  const loginUser = async (e) => {
    e.preventDefault()
    setError(null)

    try {
      const formData = {
        phone_number: e.target.phone_number.value,
        password: e.target.password.value,
      }

      const { data } = await axios.post('http://localhost:8000/auth/token/', formData)

      const decoded = jwtDecode(data.access)
      const tokens = {
        access: data.access,
        refresh: data.refresh,
      }

      setAuthTokens(tokens)
      setUser(decoded)
      localStorage.setItem('authTokens', JSON.stringify(tokens))
      routeBasedOnRole(decoded.role)
    } catch (err) {
      console.error('Login error:', err)
      setError('Invalid credentials. Please try again.')
    }
  }

  const logoutUser = useCallback(() => {
    setAuthTokens(null)
    setUser(null)
    localStorage.removeItem('authTokens')
    router.push('/')
  }, [router])

  const updateToken = useCallback(async () => {
    if (!authTokens?.refresh) {
      logoutUser()
      return
    }

    try {
      const { data } = await axios.post('http://localhost:8000/auth/token/refresh/', {
        refresh: authTokens.refresh,
      })

      const updatedTokens = {
        access: data.access,
        refresh: authTokens.refresh,
      }

      setAuthTokens(updatedTokens)
      const decoded = jwtDecode(data.access)
      setUser(decoded)
      localStorage.setItem('authTokens', JSON.stringify(updatedTokens))
    } catch (err) {
      console.error('Token refresh error:', err)
      logoutUser()
    }
  }, [authTokens, logoutUser])

  useEffect(() => {
    if (!authTokens) return

    const interval = setInterval(updateToken, REFRESH_INTERVAL_MS)
    return () => clearInterval(interval)
  }, [authTokens, updateToken])

  const contextValue = useMemo(() => ({
    user,
    authTokens,
    loginUser,
    logoutUser,
    error,
    isAuthenticated: !!user,
  }), [user, authTokens, error, logoutUser])

  return (
    <AuthContext.Provider value={contextValue}>
      {loading ? <div>Loading...</div> : children}
    </AuthContext.Provider>
  )
}
