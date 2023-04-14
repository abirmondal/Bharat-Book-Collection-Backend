from sqlalchemy import text
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import DatabaseError
from fastapi import HTTPException
import bcrypt
import datetime
import random
import string
from models import *
from database import engine

def checkUser(user, password):
    result = []
    qStr = '''
    SELECT user_id, username, name, password, email,
    gender_name as gender, gender_symbol, age
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


def __unameEmailExist(uname, email):
    result = []
    qStr = '''
    SELECT * FROM user_det
    WHERE username=:uname
    OR email=:email
    '''
    query = text(qStr)
    with engine.connect() as con:
        try:
            rs = con.execute(query, {"uname": uname, "email": email})
            con.close()
            for row in rs:
                result.append(row)
            if len(result) != 0:
                return True
        except DatabaseError as ex:
            raise HTTPException(status_code=400, detail=str(ex.orig))
    return False

def __genID():
    idStr = "id"
    monStrs = ['JA', 'FE', 'MR', 'AP', 'MA', 'JN', 'JY', 'AG', 'SE', 'OC', 'NV', 'DE']
    dateVal = datetime.datetime.now()
    idStr += str(dateVal.day)
    idStr += monStrs[dateVal.month - 1]
    idStr += str(dateVal.year)
    idStr += ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return idStr

def addUser(userDet):
    result = []
    qStr = '''
    INSERT INTO user_det(user_id, username, name, email,
    password, gender, age)
    VALUES (:id, :username, :name, :email, :password, :gender, :age)
    '''
    query = text(qStr)
    with engine.connect() as con:
        try:
            userjson = jsonable_encoder(userDet)
            userjson["id"] = __genID()
            if __unameEmailExist(userjson["username"], userjson["email"]) == True:
                raise HTTPException(
                    status_code=409, detail="Username or email id exists!")
            userjson["password"] = bcrypt.hashpw(
                userjson["password"].encode('ASCII'), bcrypt.gensalt()).decode('ASCII')
            rs = con.execute(query, userjson)
            con.commit()
            con.close()
            result.append({"message": "User account created."})
        except DatabaseError as ex:
            raise HTTPException(status_code=400, detail=str(ex.orig))

    return result
