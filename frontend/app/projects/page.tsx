import ChatWidget from "@/components/ChatWidget";

export default function Projects() {
  return (
    <main className="container mx-auto p-6 space-y-8">
      <h1 className="text-3xl font-bold">Projects</h1>
      <ChatWidget endpoint="/api/projects" agentName="ProjectAgent" />
    </main>
  );
}
