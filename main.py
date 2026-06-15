from fastapi import FastAPI
from pydantic import BaseModel
from collections import Counter

app = FastAPI()

class InputData(BaseModel):
    history: list[int]

def size_of(n):
    return "Big" if n >= 5 else "Small"

@app.post("/predict")
def predict(data: InputData):
    sizes = [size_of(x) for x in data.history]

    big_count = sizes.count("Big")
    small_count = sizes.count("Small")

    prediction = "Big" if big_count >= small_count else "Small"

    return {
        "prediction": prediction
    }