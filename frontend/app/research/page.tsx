import ChatWidget from "@/components/ChatWidget";

export default function Research() {
  return (
    <main className="container mx-auto p-6 space-y-8">
      <h1 className="text-3xl font-bold">Research</h1>
      <ChatWidget endpoint="/api/research" agentName="ResearchAgent" />
    </main>
  );
}
