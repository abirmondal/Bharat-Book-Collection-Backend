from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from DBoperations import *
from models import *
from MLFunctions import *


description = '''
This is the api docs page for Bharat Book Collection project.<br>
It is a *B.Tech.* Project.

Contributors
* Abir Mondal
* Arnab Mukhopadyay
* Debjoy Sarkar
* Dipen Hore
* Kingshuk Roy
* Somak Bose

Links
* [GitHub Repo Link](https://github.com/abirmondal/Bharat-Book-Collection-Backend)
* [Frontend Repo Link]()
'''

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** and **signup** logic is also here.",
    }
]

app = FastAPI(
    title="Bharat Book Collection Backend",
    description=description,
    version="0.1.0",
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

from fastapi.responses import RedirectResponse
@app.get("/", include_in_schema=False)
async def docs_redirect():
    response = RedirectResponse(url='/docs')
    return response

@app.post("/login/", tags=['users'])
def loginAuth(user: UserLogin):
    return checkUser(user.username, user.password)


@app.post("/signup/", tags=['users'])
def loginAuth(user: UserDet):
    return addUser(user)

@app.get("/get-book-details/", tags=['recommend'])
def getBookDet(isbn: str):
    return getBookbyISBN(isbn)