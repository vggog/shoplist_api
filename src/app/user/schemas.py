from pydantic import BaseModel


class EmailSchema(BaseModel):
    email: str


class UserAuthCode(EmailSchema):
    code: int
