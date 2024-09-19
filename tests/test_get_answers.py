from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from config.database import Base
from main import app, get_db
from schemas.answer import CreateAnswer
from services.answer import create_answer
from services.pic import create_pic

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def setup():
    db = TestingSessionLocal()
    qas = [
        ("What object stands out in the image?", "chapil"),
        ("What color is the sky?", "green"),
        ("What activity are they doing here?", "coding"),
        ("How they are looking?", "desgualangado"),
        ("What is the animal in the image?", "cuy"),
    ]

    pics = [create_pic(db, f"image-{i}.png") for i in range(5)]
    _ = [
        create_answer(
            db,
            CreateAnswer(question=qa[0], answer=qa[1], pic_id=pic.id)
        )
        for qa, pic in zip(qas, pics)
    ]

    db.close()


def test_get_answers():
    setup()
    response = client.get("/answer/")

    assert response.status_code == 200
    assert response.json()[:2] == [
        {
            "id": 1,
            "question": "What object stands out in the image?",
            "answer": "chapil",
            "pic_id": 1,
        },
        {
            "id": 2,
            "question": "What color is the sky?",
            "answer": "green",
            "pic_id": 2,
        }
    ]


def test_get_answer():
    setup()
    response = client.get("/answer/1/")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "question": "What object stands out in the image?",
        "answer": "chapil",
        "pic_id": 1,
    }

