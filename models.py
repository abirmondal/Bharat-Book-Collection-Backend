from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class UserDet(BaseModel):
    username: str
    name: str
    email: str
    password: str
    gender: int
    age: int
