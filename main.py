from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get("/posts")
def getPost():
    return {"message": "this is your post"}

@app.post("/predict")
def postreq(payload: dict= Body(...)):
    print(payload)
    return {"message": payload}