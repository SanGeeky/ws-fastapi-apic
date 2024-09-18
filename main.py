from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/greeting/{name}")
def read_item(name: str, q: Union[str, None] = None):
    return {"greeting": f"Hey {name}, you're the best 🫶.", "q": q}
