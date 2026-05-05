const BASE_URL = import.meta.env.VITE_BACKEND_URL;

export const sendMessageAPI = async (message) => {
  try {
    const res = await fetch(`${BASE_URL}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    if (!res.ok) {
      throw new Error("Failed to fetch response from server");
    }

    return await res.json();
  } catch (error) {
    console.error("API Error:", error);
    return { response: "Error connecting to backend ??" };
  }
};