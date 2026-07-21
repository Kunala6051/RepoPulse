import ChatWindow from "../components/chat/ChatWindow";

export default function AIChat() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">AI Chat (Q&amp;A)</h1>
      <p className="text-sm text-gray-500">Ask plain-language questions grounded in the current repo state.</p>
      <div className="mt-6">
        <ChatWindow />
      </div>
    </div>
  );
}
