from sqlalchemy.orm import Session
import uuid

from app.db.models import Document, Chunk
from app.ingestion.chunker import chunk_text
from app.retrieval.embeddings import EmbeddingService
from app.retrieval.vector_store import VectorStore


def ingest_document(
    db: Session,
    title: str | None,
    filename: str | None,
    text: str,
):
    """
    Full ingestion pipeline:
    - Save document
    - Chunk text
    - Save chunks
    - Embed chunks
    - Store vectors
    """

    # 1. Create document
    document = Document(
        title=title,
        filename=filename,
        text=text,
    )
    db.add(document)
    db.commit()
    db.refresh(document)

    # 2. Chunk text
    chunks = chunk_text(text)

    chunk_objects: list[Chunk] = []

    for c in chunks:
        chunk_obj = Chunk(
            document_id=document.id,
            chunk_text=c["text"],
            start_pos=c["start"],
            end_pos=c["end"],
        )
        db.add(chunk_obj)
        chunk_objects.append(chunk_obj)

    db.commit()

    # 3. Generate embeddings
    embedder = EmbeddingService()
    texts = [c.chunk_text for c in chunk_objects]
    embeddings = embedder.embed(texts)

    # 4. Prepare vector-store payload
    chunk_ids = [str(uuid.uuid4()) for _ in chunk_objects]

    metadatas = [
        {
            "document_id": document.id,
            "chunk_id": chunk.id,
            "title": title,
            "filename": filename,
        }
        for chunk in chunk_objects
    ]

    # 5. Store vectors
    vector_store = VectorStore()
    vector_store.add_embeddings(
        ids=chunk_ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas,
    )

    db.refresh(document)
    return document
