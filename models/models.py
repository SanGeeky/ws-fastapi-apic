from sqlalchemy import Column, ForeignKey, Integer, String, TEXT
from sqlalchemy.orm import relationship

from config.database import Base


class Pic(Base):
    __tablename__ = "pics"

    id = Column(Integer, primary_key=True)
    image = Column(TEXT)

    answers = relationship("Answer", back_populates="pics")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)
    pic_id = Column(Integer, ForeignKey("pics.id"))

    pics = relationship("Pic", back_populates="answers")
