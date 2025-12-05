# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.database import Base, engine, get_db
from app.db import models
from app.schemas.query import DocumentCreate, DocumentResponse

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/documents", response_model=DocumentResponse)
def create_document(doc: DocumentCreate, db: Session = Depends(get_db)):
    new_doc = models.Document(
        title=doc.title,
        filename=doc.filename,
        text=doc.text,
        source=doc.source
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

@app.get("/")
def root():
    return {"message": "RAG Assistant API is running"}
