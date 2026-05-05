import MessageBubble from "./MessageBubble";
import Loader from "./Loader";

export default function ChatWindow({ messages, loading }) {
  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-3 bg-white rounded-xl shadow">
      {messages.map((msg, index) => (
        <MessageBubble key={index} msg={msg} />
      ))}

      {loading && <Loader />}
    </div>
  );
}