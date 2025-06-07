from pydantic import BaseModel
from typing import Optional


class GuguCalculateRequest(BaseModel):
    n: int


class GeneralResponse(BaseModel):
    status: str
    is_error: bool
    result: Optional[str | int]
