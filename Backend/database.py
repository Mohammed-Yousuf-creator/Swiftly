from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase , sessionmaker
import os
from dotenv import load_dotenv


load_dotenv('db_key.env')

Database_url_link = os.getenv('DATABASE_URL_LINK')

if not Database_url_link:
    raise ValueError("Database URL is missing! Check your secret.env file.")

engine = create_engine(Database_url_link)

Session_local = sessionmaker(autoflush= False , autocommit = False , bind=engine)

class Base(DeclarativeBase):
    pass