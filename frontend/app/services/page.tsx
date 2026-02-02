import ChatWidget from "@/components/ChatWidget";

export default function Services() {
  return (
    <main className="container mx-auto p-6 space-y-8">
      <h1 className="text-3xl font-bold">Services</h1>
      <ChatWidget endpoint="/api/services" agentName="BusinessAdvisor" />
    </main>
  );
}
