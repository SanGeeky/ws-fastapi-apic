from sqlalchemy.orm import Session

from models.models import Pic


def get_pic(db: Session, pic_id: int):
    return db.query(Pic).filter(Pic.id == pic_id).first()


def get_pics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pic).offset(skip).limit(limit).all()


def create_pic(db: Session, image: str):
    db_image = Pic(image=image)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image
