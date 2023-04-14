from pydantic import BaseModel

class UserDet(BaseModel):
    username: str
    name: str
    email: str
    password: str
    gender: int
    age: int
