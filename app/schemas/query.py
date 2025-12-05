# app/schemas/query.py
from pydantic import BaseModel
from typing import Optional

class DocumentCreate(BaseModel):
    title: Optional[str]
    filename: Optional[str]
    text: Optional[str]
    source: Optional[str] = None

class DocumentResponse(BaseModel):
    id: int
    title: Optional[str]
    filename: Optional[str]

    class Config:
        orm_mode = True
