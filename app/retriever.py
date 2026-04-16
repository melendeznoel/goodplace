from app.embeddings import embed
from app.config import TOP_K

def retriever(query: str, vector_store):
    query_embedding = embed(query)
    return vector_store.search(query_embedding, top_k=TOP_K)
