"use client";
import React, { useState } from "react";
import MarkdownView from "./MarkdownView";

type Props = { endpoint: string; agentName: string };

export default function ChatWidget({ endpoint, agentName }: Props) {
  const [q, setQ] = useState("");
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [md, setMd] = useState<string>("");

  const ask = async () => {
    setLoading(true); setErr(null);
    try {
      const r = await fetch(`${process.env.NEXT_PUBLIC_API_URL}${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: q }),
        credentials: "include",
      });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      const data = await r.json();
      setMd(data.markdown || "");
    } catch (e: any) {
      setErr(e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="border rounded-lg p-4 bg-white/50 dark:bg-zinc-900/50">
      <div className="flex items-center gap-2 mb-3">
        <div className="h-8 w-8 rounded-full bg-indigo-600" />
        <div className="font-semibold">{agentName}</div>
      </div>
      <div className="flex gap-2">
        <input className="flex-1 border px-3 py-2 rounded"
               placeholder="Ask something…" value={q} onChange={e => setQ(e.target.value)} />
        <button onClick={ask} disabled={loading || !q.trim()} 
                className="bg-indigo-600 text-white px-4 py-2 rounded disabled:opacity-50">
          {loading ? "Thinking…" : "Ask"}
        </button>
      </div>
      {err && <div className="text-red-600 mt-2 text-sm">Error: {err}</div>}
      {md && <div className="mt-4"><MarkdownView content={md} /></div>}
    </div>
  );
}
