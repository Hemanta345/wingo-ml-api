from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    history: list[int]

def size_of(n):
    return "Big" if n >= 5 else "Small"

@app.post("/predict")
def predict(data: InputData):
    history = data.history

    if len(history) < 5:
        return {
            "prediction": "Big",
            "confidence": 50,
            "engine": "Fallback"
        }

    sizes = [size_of(x) for x in history]

    # Trend
    big_count = sizes.count("Big")
    small_count = sizes.count("Small")
    trend = "Big" if big_count >= small_count else "Small"

    # Streak Detector
    streak = None
    if len(sizes) >= 3:
        if sizes[0] == sizes[1] == sizes[2]:
            streak = "Small" if sizes[0] == "Big" else "Big"

    # ZigZag Detector
    zigzag = None
    if len(sizes) >= 4:
        a, b, c, d = sizes[0], sizes[1], sizes[2], sizes[3]
        if a != b and b != c and c != d:
            zigzag = "Small" if a == "Big" else "Big"

    # Final Decision
    prediction = zigzag or streak or trend

    confidence = round(
        max(big_count, small_count) / len(sizes) * 100
    )

    return {
        "prediction": prediction,
        "confidence": confidence,
        "engine": "Trend + Streak + ZigZag"
    }
