# app/retrieval/vector_store.py

import chromadb
from chromadb.config import Settings


class VectorStore:
    """
    Handles embedding storage and semantic search using ChromaDB.
    """

    def __init__(self, persist_directory: str = "data/chroma"):
        self.client = chromadb.Client(
            settings=Settings(
                persist_directory=persist_directory
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}  # cosine similarity for MiniLM
        )

    def add_embeddings(self, ids, embeddings, metadatas, documents):
        """
        Store embeddings and metadata.
        """
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    def similarity_search(self, query: str, top_k: int = 3):
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )
        # Format results nicely
        hits = []
        for i in range(len(results['ids'][0])):
            hits.append({
                'id': results['ids'][0][i],
                'document': results['documents'][0][i],
                'score': results['distances'][0][i]
            })
        return hits
