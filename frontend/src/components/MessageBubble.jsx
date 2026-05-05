export default function MessageBubble({ msg }) {
  return (
    <div
      className={`p-3 rounded-xl max-w-lg whitespace-pre-wrap ${
        msg.role === "user"
          ? "ml-auto bg-blue-500 text-white"
          : "mr-auto bg-gray-200 text-black"
      }`}
    >
      {msg.content}
    </div>
  );
}