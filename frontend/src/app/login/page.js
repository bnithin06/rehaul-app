'use client'

import { useContext } from 'react'
import AuthContext from '@/context/AuthContext'

export default function LoginPage() {
  const { loginUser, error } = useContext(AuthContext)

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form onSubmit={loginUser} className="bg-white p-6 rounded-2xl shadow-lg w-full max-w-sm">
        <h2 className="text-2xl font-semibold text-center mb-4">Login</h2>

        {error && (
          <div className="mb-4 text-red-600 text-sm text-center">
            Invalid phone number or password
          </div>
        )}

        <div className="mb-4">
          <label htmlFor="phone_number" className="block text-sm font-medium text-gray-700">
            Phone Number
          </label>
          <input
            type="text"
            id="phone_number"
            name="phone_number"
            placeholder="Enter your phone number"
            className="mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
            required
          />
        </div>

        <div className="mb-6">
          <label htmlFor="password" className="block text-sm font-medium text-gray-700">
            Password
          </label>
          <input
            type="password"
            id="password"
            name="password"
            placeholder="Enter your password"
            className="mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500"
            required
          />
        </div>

        <button
          type="submit"
          className="w-full bg-indigo-600 text-white py-2 rounded-md hover:bg-indigo-700 transition cursor-pointer"
        >
          Login
        </button>
      </form>
    </div>
  )
}
