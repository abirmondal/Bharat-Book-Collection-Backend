from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from DBoperations import *


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.post("/login/", tags=['users'])
def loginAuth(username: str, password: str):
    return checkUser(username, password)



