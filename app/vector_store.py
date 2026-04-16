import numpy as np

class VectorStore:
    def __init__(self):
        self.items = []

    def add(self, text: str, embedding: list[float]):
        self.items.append({
            "text": text,
            "embedding": embedding
        })
    
    def _cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def search(self, query_embedding, top_k=3):
        scored = []

        for item in self.items:
            score = self._cosine_similarity(query_embedding, item["embedding"])
            scored.append((score, item["text"]))

        scored.sort(reverse=True)

        return [text for _, text in scored[:top_k]]
