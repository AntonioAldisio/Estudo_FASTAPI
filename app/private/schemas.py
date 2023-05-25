from pydantic import BaseModel


class UserInfoResponse(BaseModel):
    login: str
    nome: str
    email: str
    status: bool


class messageResponse(BaseModel):
    message: str
