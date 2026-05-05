from sentence_transformers import SentenceTransformer

# Load embedding model once (global)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text: str):
    """
    Convert a single text string into a vector embedding
    """
    return model.encode(text)


def embed_batch(texts: list):
    """
    Convert a list of texts into embeddings
    """
    return model.encode(texts)