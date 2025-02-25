from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content : str
    published : bool =True
    rating : Optional[int] = None

@app.get("/posts")
def getPost():
    return {"message": "this is your post"}

@app.post("/predict")
def postreq(post: Post):
    print(post)
    print(post.model_dump())
    return {"message": post}