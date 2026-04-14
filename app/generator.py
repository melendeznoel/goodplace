import ollama

from .config import (LLM_MODEL)


def generate(query: str, context_chunks: list[str]) -> str:
    """Generate an answer to a query using the provided context chunks."""
    context = "\n\n".join(context_chunks)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model=LLM_MODEL,
        prompt=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
