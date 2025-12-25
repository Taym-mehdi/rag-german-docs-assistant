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

    def search(self, query_embedding, n_results=5):
        """
        Perform semantic search.
        """
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )
