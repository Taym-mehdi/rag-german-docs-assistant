# app/ingestion/ingest.py
from sqlalchemy.orm import Session
from app.db.models import Document, Chunk
from app.ingestion.chunker import simple_chunk_text

def ingest_document(db: Session, title: str, filename: str, text: str) -> Document:

    document = Document(
        title=title,
        filename=filename,
        text=text
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    chunks = simple_chunk_text(text)

    for chunk_text, start, end in chunks:
        chunk = Chunk(
            document_id=document.id,
            chunk_text=chunk_text,
            start_pos=start,
            end_pos=end
        )
        db.add(chunk)

    db.commit()
    db.refresh(document)

    return document
