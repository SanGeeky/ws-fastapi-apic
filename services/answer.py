from sqlalchemy.orm import Session

from models.models import Answer
from schemas.answer import CreateAnswer


def get_answer(db: Session, answer_id: int):
    return db.query(Answer).filter(Answer.id == answer_id).first()


def get_answers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Answer).offset(skip).limit(limit).all()


def create_answer(db: Session, answer: CreateAnswer):
    db_answer = Answer(**answer.model_dump())
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


def update_answer(db: Session, answer_id: int, answer: CreateAnswer):
    db_answer = db.query(Answer).filter(Answer.id == answer_id).first()
    db_answer.answer = answer.answer
    db_answer.question = answer.question
    db.commit()
    return db_answer


def delete_movie(db: Session, answer_id: int):
    db.query(Answer).filter(Answer.id == answer_id).delete()
    db.commit()
