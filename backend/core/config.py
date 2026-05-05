import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Settings:
    # =========================
    # 🔹 App Settings
    # =========================
    APP_NAME: str = "Mini GPT"
    DEBUG: bool = True

    # =========================
    # 🔹 LLM Settings
    # =========================
    USE_API: bool = os.getenv("USE_API", "true").lower() == "true"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    MODEL_NAME: str = os.getenv(
        "MODEL_NAME",
        "gpt-4o-mini"  # default API model
    )

    # =========================
    # 🔹 Embedding Settings
    # =========================
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )

    # =========================
    # 🔹 Vector DB Settings
    # =========================
    VECTOR_DB_PATH: str = os.getenv(
        "VECTOR_DB_PATH",
        "db/faiss_index"
    )
    TOP_K: int = int(os.getenv("TOP_K", 3))

    # =========================
    # 🔹 Prompt Settings
    # =========================
    SYSTEM_PROMPT: str = os.getenv(
        "SYSTEM_PROMPT",
        "You are a helpful AI assistant."
    )


# Create a single settings instance
settings = Settings()