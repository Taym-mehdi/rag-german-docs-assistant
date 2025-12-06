#app/ingestion/chunker.py

from typing import List

def simple_chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Split text into overlapping chunks.
    Example:
        chunk1: 0-500
        chunk2: 450-950
    Overlap helps the model keep context.
    """
    if not text : 
        return []
    
    chunks = []
    start = 0 

    while start < len (text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append((chunk, start, end))
        start = end - overlap

    return chunks
