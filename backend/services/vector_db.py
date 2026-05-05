
from backend.core.config import settings
import faiss
import numpy as np
import os
import pickle

from services.embeddings import embed_text

# =========================
# 🔹 Config
# =========================
DIMENSION = 384  # for all-MiniLM-L6-v2
DB_PATH = settings.VECTOR_DB_PATH

# =========================
# 🔹 Initialize DB
# =========================
if os.path.exists(f"{DB_PATH}.index"):
    index = faiss.read_index(f"{DB_PATH}.index")

    with open(f"{DB_PATH}.pkl", "rb") as f:
        documents = pickle.load(f)
else:
    index = faiss.IndexFlatL2(DIMENSION)
    documents = []


# =========================
# 🔹 Store Message
# =========================
def store_message(user_msg: str, bot_msg: str):
    """
    Store conversation into vector DB
    """
    combined_text = f"User: {user_msg} Bot: {bot_msg}"

    vector = embed_text(combined_text)
    vector = np.array([vector]).astype("float32")

    index.add(vector)
    documents.append(combined_text)

    _save_db()


# =========================
# 🔹 Retrieve Context
# =========================
def retrieve_context(query: str, k: int = 3):
    """
    Get top-k similar past messages
    """
    if len(documents) == 0:
        return []

    query_vector = embed_text(query)
    query_vector = np.array([query_vector]).astype("float32")

    distances, indices = index.search(query_vector, k)

    results = []
    for i in indices[0]:
        if i < len(documents):
            results.append(documents[i])

    return results


# =========================
# 🔹 Save DB
# =========================
def _save_db():
    """
    Persist FAISS index + documents
    """
    os.makedirs("db", exist_ok=True)

    faiss.write_index(index, f"{DB_PATH}.index")

    with open(f"{DB_PATH}.pkl", "wb") as f:
        pickle.dump(documents, f)