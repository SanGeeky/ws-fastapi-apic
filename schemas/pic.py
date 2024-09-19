from pydantic import BaseModel

from schemas.answer import Answer


class BasePic(BaseModel):
    image: str


class CreatePic(BasePic):
    pass


class Pic(BaseModel):
    id: int
    answers: list[Answer] = []

    class Config:
        from_attributes = True
