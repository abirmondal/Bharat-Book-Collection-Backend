import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

dbHost = os.getenv('DB_HOST')
dbName = os.getenv('DB_NAME')
dbUser = os.getenv('DB_USERNAME')
dbPass = urllib.parse.quote(os.getenv('DB_PASSWORD'))

DATABASE_URL = "mysql+mysqlconnector://" + dbUser + \
    ":" + dbPass + "@" + dbHost + ":3306/" + dbName
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
