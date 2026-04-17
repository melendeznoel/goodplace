from app import (
    load_text, chunk_text,
    embed, VectorStore, retriever,
    generate
)
from app.config import CHUNK_SIZE


class RagPipeline:
    def __init__(self):
        self.vector_store = VectorStore()

    def ingest(self, file_path: str):
        text = load_text(file_path)

        chunks = chunk_text(text, CHUNK_SIZE)

        for chunk in chunks:
            emb = embed(chunk)

            self.vector_store.add(chunk, emb)

    def query(self, question: str) -> str:
        context = retriever(question, self.vector_store)

        return generate(question, context)
