from sqlalchemy.orm import Session

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

    # 1️⃣ Create document
    document = Document(
        title=title,
        filename=filename,
        text=text,
    )
    db.add(document)
    db.commit()
    db.refresh(document)

    # 2️⃣ Chunk text
    chunks = chunk_text(text)

    chunk_objects = []
    for idx, c in enumerate(chunks):
        chunk_obj = Chunk(
            document_id=document.id,
            chunk_text=c["text"],
            start_pos=c["start"],
            end_pos=c["end"],
        )
        db.add(chunk_obj)
        chunk_objects.append(chunk_obj)

    db.commit()
    db.refresh(document)

    # 3️⃣ Generate embeddings
    embedder = EmbeddingService()
    texts = [c.chunk_text for c in chunk_objects]
    embeddings = embedder.embed(texts)

    # 4️⃣ Store embeddings in vector store
    vector_store = VectorStore()

    chunk_ids = [str(c.id) for c in chunk_objects]  # unique IDs
    metadatas = [
        {
            "document_id": c.document_id,
            "chunk_index": idx,
            "filename": document.filename
        }
        for idx, c in enumerate(chunk_objects)
    ]

    vector_store.add_embeddings(
        ids=chunk_ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas
    )

    # 5️⃣ Return the document
    return document
