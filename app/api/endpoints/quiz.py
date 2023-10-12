from typing import Union, List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db, take_unique_questions
from app.api.schemas.quiz import QuizCreate, QuizResponse
from app.db.cruds import crud_quiz

router = APIRouter()


@router.post("/questions", response_model=Union[List[QuizResponse], List])
def create_question(questions_num: int, db: Session = Depends(get_db)):
    """
    **Create a new question.**

    - :param **questions_num:** The number of unique questions to create.
    - :param **db:** The database session.
    - :return: List of newly created questions or an empty list if no data is available.
    """
    data = take_unique_questions(questions_num)

    # Если данных нет, возвращаем пустой список
    if not data:
        return []

    new_quiz_list = []
    for quiz in data:
        db_quiz = crud_quiz.get_question(db, question_id=quiz['id'])
        # Если вопрос уже существует в базе данных
        if db_quiz:
            # Извлекаем новый из jService API
            new_data = take_unique_questions(1)
            data.append(new_data)
        # Если вопроса еще нет в базе данных
        else:
            # Создаем новый вопрос и сохраняем его в базе данных
            new_quiz_to_db = QuizCreate(
                question_id=quiz["id"],
                question_text=quiz["question"],
                answer_text=quiz["answer"]
            )
            db_quiz = crud_quiz.create_question(db, new_quiz_to_db)
            new_quiz_list.append(db_quiz)

    # Извлекаем последний добавленный вопрос
    last_added_quiz = new_quiz_list[-1]

    return [last_added_quiz]
