# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.ingestion.ingest import ingest_document
from app.db.database import Base, engine

from pydantic import BaseModel

# Create tables on start (development only)
Base.metadata.create_all(bind=engine)

class DocumentCreate(BaseModel):
    title: str | None = None
    filename: str | None = None
    text: str
    

app = FastAPI()


@app.post("/documents")
def upload_document(doc: DocumentCreate, db: Session = Depends(get_db)):

    document = ingest_document(
        db=db,
        title=doc.title,
        filename=doc.filename,
        text=doc.text
    )

    return {
        "id": document.id,
        "title": document.title,
        "filename": document.filename,
        "uploaded_at": document.uploaded_at.isoformat(),
        "chunks": len(document.chunks)
    }
