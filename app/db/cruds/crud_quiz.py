from typing import Union

from sqlalchemy.orm import Session

from app.api.schemas.quiz import QuizBase
from app.db.models.quiz import Quiz


def get_question(db: Session, question_id: int) -> Union[Quiz, None]:
    """
    Retrieve a question from the database by its ID.

    :param db: The database session.
    :param question_id: The ID of the question to retrieve.
    :return: The retrieved question.
    """
    return db.query(Quiz).filter(Quiz.question_id == question_id).first()


def create_question(db: Session, quiz: QuizBase) -> Quiz:
    """
    Create a new question and save it to the database.

    :param db: The database session.
    :param quiz: The data of the question to create.
    :return: The newly created question.
    """
    db_quiz = Quiz(
        question_id=quiz.question_id,
        question_text=quiz.question_text,
        answer_text=quiz.answer_text
    )
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz
