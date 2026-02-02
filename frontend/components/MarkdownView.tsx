"use client";
import React from "react";
import ReactMarkdown from "react-markdown";

export default function MarkdownView({ content }: { content: string }) {
  return <div className="prose prose-slate dark:prose-invert max-w-none"><ReactMarkdown>{content}</ReactMarkdown></div>;
}
