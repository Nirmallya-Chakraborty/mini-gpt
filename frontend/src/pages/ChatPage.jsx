import useChat from "../hooks/useChat";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";

export default function ChatPage() {
  const { messages, loading, sendMessage } = useChat();

  return (
    <div className="flex flex-col h-screen bg-gray-100 p-4">
      
      {/* Header */}
      <h1 className="text-xl font-bold mb-3">Mini GPT</h1>

      {/* Chat messages */}
      <ChatWindow messages={messages} loading={loading} />

      {/* Input box */}
      <div className="mt-3">
        <ChatInput onSend={sendMessage} />
      </div>
    </div>
  );
}