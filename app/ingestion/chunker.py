#app/ingestion/chunker.py

from typing import List

def chunk_text(
        text: str,
        chunk_size: int = 500,
        overlap: int = 50
):
    
    """
    Split text into overlapping chunks.
    Returns list of dicts with text + positions.

    """
    if not text : 
        return []
    
    chunks = []
    start = 0 
    length = len(text)


    while start < length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append({
            "text": chunk,
            "start": start,
            "end": min(end, length),
        })

        start = end - overlap

    return chunks
