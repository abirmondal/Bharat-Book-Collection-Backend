from sqlalchemy import text
from fastapi.encoders import jsonable_encoder
from database import engine
from sqlalchemy.exc import DatabaseError
from fastapi import HTTPException
import bcrypt

def checkUser(user, password):
    result = []
    query = text("SELECT * FROM user_det WHERE username=:username;")
    with engine.connect() as con:
        try:
            rs = con.execute(query, {"username": user})
            con.close()
            for row in rs:
                userResult = jsonable_encoder(row._asdict())
                passHash = userResult['password'].encode('ASCII')
                encodedPassword = password.encode('ASCII')
                if bcrypt.checkpw(encodedPassword, passHash):
                    result.append(userResult)
            if len(result) == 0:
                raise HTTPException(status_code=401, detail="Username or Password is incorrect!")
        except DatabaseError as ex:
            raise HTTPException(status_code=400, detail=str(ex.orig))

    return result
