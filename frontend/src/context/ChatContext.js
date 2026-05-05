import { createContext, useContext } from "react";
import useChat from "../hooks/useChat";

// create context
const ChatContext = createContext();

// provider component
export function ChatProvider({ children }) {
  const chat = useChat();

  return (
    <ChatContext.Provider value={chat}>
      {children}
    </ChatContext.Provider>
  );
}

// custom hook to use context
export function useChatContext() {
  return useContext(ChatContext);
}