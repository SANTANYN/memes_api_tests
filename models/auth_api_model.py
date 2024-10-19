from pydantic import BaseModel


class AuthApiResponse(BaseModel):
    token: str
    user: str
