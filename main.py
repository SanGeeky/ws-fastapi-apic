import io
from random import choice

from fastapi import FastAPI, UploadFile
from PIL import Image

from services.visual_question_answer import VisualQuestionAnswering

app = FastAPI()
model = VisualQuestionAnswering()
emojis = ["🤫", "🤩", "🧐", "🤠", "👀", "✅", "🧚", "🥳", "🥸"]


@app.post("/ask")
def ask(question: str, image: UploadFile):
    content = image.file.read()

    image = Image.open(io.BytesIO(content))

    result = model.pipeline(question, image)
    return {"answer": f"{result} {choice(emojis)}"}


@app.get("/")
def read_root():
    return {"Hello": "World"}
