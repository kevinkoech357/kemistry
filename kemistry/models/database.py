import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv(".env")

DATABASE_HOST = os.environ.get("DATABASE_HOST")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

connection_string = URL.create(
    "postgresql",
    username="DATABASE_USER",
    password="DATABASE_PASSWORD",
    host="DATABASE_HOST",
    database="DATABASE_NAME",
)

engine = create_engine(connection_string)
"""
engine = create_engine("sqlite:///kemistry.db")
"""
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from kemistry.models.user import User, Role

    Base.metadata.create_all(bind=engine)
