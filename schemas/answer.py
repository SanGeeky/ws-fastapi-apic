from pydantic import BaseModel


class BaseAnswer(BaseModel):
    question: str
    answer: str
    pic_id: int


class CreateAnswer(BaseAnswer):
    pass


class Answer(BaseAnswer):
    id: int

    class Config:
        from_attributes = True


class ResponseAnswer(BaseModel):
    answer: str
