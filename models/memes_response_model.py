from pydantic import BaseModel
from typing import List, Any


class MemeModel(BaseModel):
    id: int
    info: dict
    tags: List[str]
    text: str
    updated_by: str
    url: str


class MemesResponseModel(BaseModel):
    data: List[MemeModel]


class DeleteMemeModel(BaseModel):
    data: Any
