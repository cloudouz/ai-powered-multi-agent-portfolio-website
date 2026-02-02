"use client";
import React, { useState, useEffect } from "react";

function getCookie(name: string) {
  if (typeof document === "undefined") return undefined;
  const v = document.cookie.split("; ").find(c => c.startsWith(name + "="));
  return v?.split("=")[1];
}

export default function Login() {
  const [email, setEmail] = useState("");
  const [pw, setPw] = useState("");
  const [msg, setMsg] = useState<string | null>(null);

  useEffect(() => {
    // Request CSRF token cookie
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/auth/csrf`, {
      method: "POST",
      credentials: "include",
    });
  }, []);

  async function submit() {
    setMsg(null);
    const csrf = getCookie("csrf_token");
    const r = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/auth/login`, {
      method: "POST",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
        ...(csrf ? { "X-CSRF-Token": csrf } : {}),
      },
      body: JSON.stringify({ email, password: pw }),
    });
    if (!r.ok) return setMsg(`Login failed (${r.status})`);
    setMsg("Logged in");
  }

  return (
    <main className="container mx-auto p-6 space-y-4">
      <h1 className="text-2xl font-semibold">Login</h1>
      <div className="flex flex-col gap-3 max-w-sm">
        <input className="border px-3 py-2 rounded" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
        <input className="border px-3 py-2 rounded" type="password" placeholder="Password" value={pw} onChange={e => setPw(e.target.value)} />
        <button onClick={submit} className="bg-indigo-600 text-white px-4 py-2 rounded">Login</button>
        {msg && <div className="text-sm">{msg}</div>}
      </div>
    </main>
  );
}
