import requests
from typing import List

from sqlalchemy.orm import Session

from app.db.setup import SessionLocal


def get_db() -> Session:
    """
    Create a new database session and provide it for dependency injection.
    
    :return: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def take_unique_questions(number_of_questions: int) -> List[dict]:
    """
    Retrieve a specified number of unique random questions from the jService API.
    
    :param number_of_questions: The number of unique questions to retrieve.
    :return: A list of dictionaries containing the retrieved questions.
    """
    
    url = f"https://jservice.io/api/random?count={number_of_questions}"
    response = requests.get(url)
    data = response.json()
    return data
