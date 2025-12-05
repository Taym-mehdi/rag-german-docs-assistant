# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.db.database import engine, Base, SessionLocal, get_db
from sqlalchemy.orm import Session
from app.db import models

# create tables (development convenience)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RAG Q&A Assistant for German Documents",
    version="0.1.0"
)

# Pydantic schemas
class DocumentCreate(BaseModel):
    title: Optional[str] = None
    filename: Optional[str] = None
    source: Optional[str] = None
    text: Optional[str] = None

class DocumentOut(BaseModel):
    id: int
    title: Optional[str]
    filename: Optional[str]
    source: Optional[str]
    uploaded_at: Optional[str]
    text: Optional[str]

    class Config:
        orm_mode = True

# simple root
@app.get("/")
def root():
    return {"message": "RAG German Docs Assistant - Day 2 DB ready!"}

# create document endpoint
@app.post("/documents", response_model=DocumentOut)
def create_document(doc_in: DocumentCreate, db: Session = Depends(get_db)):
    doc = models.Document(
        title=doc_in.title,
        filename=doc_in.filename,
        source=doc_in.source,
        text=doc_in.text
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

# get document by id
@app.get("/documents/{document_id}", response_model=DocumentOut)
def get_document(document_id: int, db: Session = Depends(get_db)):
    doc = db.get(models.Document, document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc
