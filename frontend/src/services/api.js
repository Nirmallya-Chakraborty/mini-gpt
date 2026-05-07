const API_URL = "http://192.168.1.185:8001";

export const sendMessageAPI = async (message) => {
  try {
    const response = await fetch(`${API_URL}/api/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error("Failed to fetch response from server");
    }

    return await response.json();

  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};