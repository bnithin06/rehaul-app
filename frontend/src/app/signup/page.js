"use client";

import { useState, useContext } from "react";
import axios from "axios";
import AuthContext from "@/context/AuthContext"; // adjust path if needed

export default function Register() {
  const [formData, setFormData] = useState({
    phone_number: "",
    username: "",
    password: "",
    password2: "",
    role: "driver",
  });

  const [message, setMessage] = useState("");
  const { loginUser } = useContext(AuthContext); // 💡 Access login function

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      // 1. Register user
      await axios.post("http://127.0.0.1:8000/auth/register/", formData);
      setMessage("✅ Registered Successfully! Logging in...");

      // 2. Wait 3 seconds → Then auto-login
      setTimeout(() => {
        const fakeEvent = {
          preventDefault: () => {},
          target: {
            phone_number: { value: formData.phone_number },
            password: { value: formData.password },
          },
        };
        loginUser(fakeEvent);
      }, 300);
    } catch (err) {
      console.error("Registration error:", err.response?.data || err.message);
      setMessage("❌ Registration Failed. Check console.");
    }
  };

  return (
    <div className="min-h-screen p-6 flex flex-col items-center justify-center">
      <h2 className="text-2xl font-bold mb-4">Register</h2>

      <form onSubmit={handleSubmit} className="w-full max-w-sm space-y-4">
        <input
          type="text"
          name="phone_number"
          placeholder="Phone Number"
          onChange={handleChange}
          required
          className="w-full border p-2 rounded"
        />
        <input
          type="text"
          name="username"
          placeholder="Username"
          onChange={handleChange}
          required
          className="w-full border p-2 rounded"
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
          required
          className="w-full border p-2 rounded"
        />
        <input
          type="password"
          name="password2"
          placeholder="Confirm Password"
          onChange={handleChange}
          required
          className="w-full border p-2 rounded"
        />
        <select
          name="role"
          onChange={handleChange}
          className="w-full border p-2 rounded"
        >
          <option value="driver">Driver</option>
          <option value="lorry_owner">Lorry Owner</option>
          <option value="business">Business Person</option>
        </select>

        <button
          type="submit"
          className="w-full bg-blue-600 text-white p-2 rounded hover:bg-blue-700"
        >
          Register
        </button>
      </form>

      {message && (
        <p className="mt-4 text-center text-sm font-medium">{message}</p>
      )}
    </div>
  );
}
