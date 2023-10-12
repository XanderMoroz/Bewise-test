from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from app.core.config import settings


def create_sqlalchemy_database_url():
    """Create a SQLAlchemy database URL"""

    user = settings.POSTGRES_USER
    password = settings.POSTGRES_PASSWORD
    host = settings.POSTGRES_HOST
    port = settings.POSTGRES_PORT
    db = settings.POSTGRES_DB

    return f"postgresql://{user}:{password}@{host}:{port}/{db}"


def create_engine_and_session():
    """Create the engine and session for SQLAlchemy"""

    sqlalchemy_database_url = create_sqlalchemy_database_url()
    my_engine = create_engine(sqlalchemy_database_url)

    if not database_exists(my_engine.url):
        create_database(my_engine.url)

    session_local = sessionmaker(autocommit=False, autoflush=False, bind=my_engine)

    return my_engine, session_local


engine, SessionLocal = create_engine_and_session()

Base = declarative_base()
