from typing import List

from pydantic import BaseModel, Field


class PrintItem(BaseModel):
    barcode: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=1)


class PrintRequest(BaseModel):
    items: List[PrintItem]