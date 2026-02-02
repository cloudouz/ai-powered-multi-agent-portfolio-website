import ChatWidget from "@/components/ChatWidget";

export default function Home() {
  return (
    <main className="container mx-auto p-6 space-y-8">
      <section className="space-y-2">
        <h1 className="text-3xl font-bold">Welcome</h1>
        <p>Explore projects, services, research, and career insights.</p>
      </section>
      <ChatWidget endpoint="/api/welcome" agentName="WelcomeAgent" />
    </main>
  );
}
