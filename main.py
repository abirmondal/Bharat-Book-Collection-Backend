from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from typing import Union
from DBoperations import *
from models import *
from MLFunctions import *


description = '''
This is the api docs page for Bharat Book Collection project.<br>
It is a *B.Tech.* Project.

### Contributors
* Abir Mondal
* Arnab Mukhopadyay
* Debjoy Sarkar
* Dipen Hore
* Kingshuk Roy
* Somak Bose

### Hosted Links
* [Back-end](https://bbc-backend.onrender.com/)
* [Front-end](https://roykingshuk.github.io/BBC-Frontend/)

### Links
* [GitHub Repo Link](https://github.com/abirmondal/Bharat-Book-Collection-Backend)
* [Frontend Repo Link](https://github.com/roykingshuk/BBC-Frontend)
'''

tags_metadata = [
    {
        "name": "users",
        "description": "Operations for users. The **login** and **signup** logic is also here."
    },
    {
        "name": "books-recommend",
        "description": "Operations to get **books details**, **related books** and **most popular books**."
    }
]

app = FastAPI(
    title="Bharat Book Collection Backend",
    description=description,
    version="2.2",
    openapi_tags=tags_metadata
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

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

@app.get("/get-books/", tags=['books-recommend'])
def getTopBooks(page: Union[int, None] = None):
    return getTopBooks()

@app.get("/get-book-details/", tags=['books-recommend'])
def getBookDet(isbn: str):
    return getBookbyISBN(isbn)

@app.get("/get-book-recommend/", tags=['books-recommend'])
def getBookRecommend(title: str):
    return getRecommendationByTitle(title)
