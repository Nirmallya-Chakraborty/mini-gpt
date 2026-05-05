import { useState } from "react";
import { sendMessageAPI } from "../services/api";

export default function useChat() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hello! Ask me anything 🚀" },
  ]);

  const [loading, setLoading] = useState(false);

  const sendMessage = async (input) => {
    if (!input.trim()) return;

    // add user message
    const userMessage = { role: "user", content: input };
    const updatedMessages = [...messages, userMessage];

    setMessages(updatedMessages);
    setLoading(true);

    try {
      const data = await sendMessageAPI(input);

      // add bot response
      const botMessage = {
        role: "assistant",
        content: data.response || "No response",
      };

      setMessages([...updatedMessages, botMessage]);

    } catch (error) {
      setMessages([
        ...updatedMessages,
        { role: "assistant", content: "Error connecting backend 😢" },
      ]);
    }

    setLoading(false);
  };

  return {
    messages,
    loading,
    sendMessage,
  };
}