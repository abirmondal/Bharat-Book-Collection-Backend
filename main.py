from fastapi import FastAPI, HTTPException

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
* [Back-end Repo Link](https://github.com/abirmondal/Bharat-Book-Collection-Backend)
* [Front-end Repo Link](https://github.com/roykingshuk/BBC-Frontend)
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
    version="2.3",
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

@app.get("/get-top-books/", tags=['books-recommend'])
def getTopBooksList(page: Union[int, None] = None, perPage: Union[int, None] = None):
    if page == None and perPage == None:
        return getTopBooks()
    elif page == None:
        if perPage < 1:
            raise HTTPException(status_code=400, detail="Books per page cannot be less than 1.")
        return getTopBooks(perPage=perPage)
    elif perPage == None:
        if page < 1:
            raise HTTPException(status_code=400, detail="Page number cannot be less than 1.")
        return getTopBooks(page=page)
    else:
        return getTopBooks(page, perPage)

@app.get("/get-book-details/", tags=['books-recommend'])
def getBookDet(isbn: str, perPage: Union[int, None] = None):
    perPage = perPage if perPage != None else 5

    return getBookDetAndRecommend(isbn, perPage)
