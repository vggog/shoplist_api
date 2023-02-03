from pydantic import BaseModel


class ErrorSchema(BaseModel):
    status_code: int
    detail: str
