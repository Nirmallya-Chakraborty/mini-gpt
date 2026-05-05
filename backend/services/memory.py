

from utils.helpers import format_context
from core.config import settings
from services.vector_db import retrieve_context

SYSTEM_PROMPT = settings.SYSTEM_PROMPT


def build_prompt(user_message: str, k: int = 3) -> str:
    """
    Build final prompt using:
    - System instructions
    - Retrieved memory/context
    - User input
    """

    # 1. Retrieve relevant past context
    context_chunks = retrieve_context(user_message, k=k)

    # 2. Format context nicely
    context_text = format_context(context_chunks)

    # 3. Build final prompt
    prompt = f"""
{SYSTEM_PROMPT}

Context:
{context_text}

User:
{user_message}
"""

    return prompt