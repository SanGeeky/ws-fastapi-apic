import base64
import io
from sqlalchemy.orm import Session

from fastapi import FastAPI, UploadFile, Depends
from PIL import Image

from config.database import SessionLocal, engine, Base
from schemas.answer import CreateAnswer
from services.answer import create_answer
from services.pic import create_pic
from services.visual_question_answer import VisualQuestionAnswering


Base.metadata.create_all(bind=engine)

app = FastAPI()
model = VisualQuestionAnswering()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/ask")
def ask(question: str, image: UploadFile, db: Session = Depends(get_db)):
    # Predict answer
    content = image.file.read()
    image = Image.open(io.BytesIO(content))
    model_answer = model.pipeline(question, image)

    # Store Pic
    encoded_image = base64.b64encode(content).decode('utf-8')
    pic_db = create_pic(db, encoded_image)
    # Store Answer
    answer = CreateAnswer(question=question, answer=model_answer, pic_id=pic_db.id)
    _ = create_answer(db, answer)

    return {"answer": model.format_answer}


@app.get("/")
def read_root():
    return {"Hello": "World"}
