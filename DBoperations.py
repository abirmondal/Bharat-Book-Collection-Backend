from sqlalchemy import text
from fastapi.encoders import jsonable_encoder
from database import engine
from sqlalchemy.exc import DatabaseError
from fastapi import HTTPException
import bcrypt

def checkUser(user, password):
    result = []
    qStr = '''
    SELECT user_id, username, password, email,
    gender_name as gender, gender_symbol
    FROM user_det as u, gender_det as g
    WHERE u.username=:username
    AND u.gender = g.g_id;
    '''
    query = text(qStr)
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
                    result[0].pop('password')
            if len(result) == 0:
                raise HTTPException(status_code=401, detail="Username or Password is incorrect!")
        except DatabaseError as ex:
            raise HTTPException(status_code=400, detail=str(ex.orig))

    return result
