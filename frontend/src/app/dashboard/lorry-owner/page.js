"use client";

import { useContext, useEffect } from "react";
import AuthContext from "@/context/AuthContext";
import { useRouter } from "next/navigation";

export default function LorryOwnerDashboard() {
  const { user, logoutUser, isAuthenticated } = useContext(AuthContext);
  const router = useRouter();

  useEffect(() => {
    if (!isAuthenticated || user?.role !== "lorry_owner") {
      router.push("/");
    }
  }, [isAuthenticated, user, router]);

  return (
    <div className="min-h-screen p-8 bg-gray-100 flex flex-col items-center">
      <h1 className="text-3xl font-bold mb-4">🚛 Lorry Owner Dashboard</h1>
      <p className="text-lg mb-2">
        Welcome, <span className="font-semibold">{user?.username}</span>
      </p>
      <p className="text-md mb-6">
        Role: <span className="text-green-600">{user?.role}</span>
      </p>
    </div>
  );
}
