# app/db/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), nullable=True)
    filename = Column(String(512), nullable=True)
    source = Column(String(512), nullable=True)
    uploaded_at = Column(DateTime, server_default=func.now())
    text = Column(Text, nullable=True)

    # Relationship to chunks
    chunks = relationship(
        "Chunk",
        back_populates="document",
        cascade="all, delete-orphan"
    )


class Chunk(Base):
    __tablename__ = "chunks"

    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    chunk_text = Column(Text, nullable=False)
    start_pos = Column(Integer, nullable=True)
    end_pos = Column(Integer, nullable=True)

    document = relationship("Document", back_populates="chunks")
