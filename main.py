from typing import Union
from fastapi import FastAPI
import model

app = FastAPI()
model = model.AndModel()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# /items/{item_id} 경로
# item_id 경로 매개변수(파라미터)
@app.get("/items/{item_id}") #endpoint 엔드포인트
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/predict/left/{left}/right/{right}")
def predict(left: int, right:int):
    result = model.predict([left,right])
    return {"result": result}


@app.post("/train")
def train():
    model.train()
    return {"result": "OK"}