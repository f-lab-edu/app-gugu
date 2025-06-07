from typing import Optional

from pydantic import BaseModel


class GuguCalculateRequest(BaseModel):
    n: int


class GeneralResponse(BaseModel):
    status: str
    is_error: bool
    result: Optional[str | int]
