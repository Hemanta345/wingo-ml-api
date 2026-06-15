from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    history: list[int]

@app.post("/predict")
def predict(data: InputData):
    return {
        "prediction": "Big"
    }
