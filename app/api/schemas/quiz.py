from datetime import datetime
from pydantic import BaseModel


class QuizBase(BaseModel):
    question_id: int
    question_text: str
    answer_text: str


class QuizCreate(QuizBase):
    pass


class QuizResponse(QuizBase):
    time_created: datetime

    class Config:
        orm_mode = True
