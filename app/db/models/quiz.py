from sqlalchemy import Column, DateTime, func
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.setup import Base


class Quiz(Base):
    """
    Model for storing information about questions.

    Attributes:
    - id (int): Unique identifier for the question.
    - question_id (int): Question identifier from jService API.
    - question_text (str): Question text.
    - answer_text (str): Answer text for the question.
    - time_created (datetime): Time of creation of the record.

    """
    __tablename__ = "quiz"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, index=True)
    question_text = Column(String, index=True)
    answer_text = Column(String, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
