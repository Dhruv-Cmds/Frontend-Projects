from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus
import os 
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# --------------------------------------------------------------------------------
#                               USE THIS WHEN YOU GO MANUAL

# import mysql.connector
# import os 
# from dotenv import load_dotenv

# load_dotenv()

# def get_conncection():
    
#     return mysql.connector.connect (

#         host = os.getenv("DB_HOST"),
#         user= os.getenv("DB_USER"),
#         password= os.getenv("DB_PASSWORD"),
#         database= os.getenv("DB_NAME")
#     )

# --------------------------------------------------------------------------------
