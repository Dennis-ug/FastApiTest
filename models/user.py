from pydantic import BaseModel


class User(BaseModel):
    userName: str
    email: str
    contact: int
