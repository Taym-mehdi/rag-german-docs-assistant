from pydantic import BaseModel
from datetime import datetime

class DocumentResponse(BaseModel):
    id: int
    title: str
    filename: str
    text: str
    uploaded_at: datetime   # ✅ correct type

    model_config = {
        "from_attributes": True  # replaces orm_mode=True in Pydantic v2
    }
