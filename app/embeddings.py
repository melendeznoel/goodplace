import ollama

from app.config import EMBED_MODEL

def embed(text: str) -> list[float]:
    response = ollama.embeddings(
        model=EMBED_MODEL,
        prompt=text
    )

    return response["embedding"]
