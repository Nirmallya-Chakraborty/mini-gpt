import uuid
import datetime
import re


# =========================
# 🔹 Generate Unique ID
# =========================
def generate_id() -> str:
    return str(uuid.uuid4())


# =========================
# 🔹 Current Timestamp
# =========================
def current_timestamp() -> str:
    return datetime.datetime.utcnow().isoformat()


# =========================
# 🔹 Clean Text
# =========================
def clean_text(text: str) -> str:
    """
    Basic cleaning:
    - Remove extra spaces
    - Strip unwanted characters
    """
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


# =========================
# 🔹 Format Context (for prompt)
# =========================
def format_context(context_list: list) -> str:
    """
    Convert list of context into readable string
    """
    if not context_list:
        return "No relevant context."

    return "\n".join(f"- {item}" for item in context_list)


# =========================
# 🔹 Truncate Text (for token control)
# =========================
def truncate_text(text: str, max_chars: int = 1000) -> str:
    """
    Prevent very long prompts
    """
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."