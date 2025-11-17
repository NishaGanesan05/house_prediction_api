from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
import pickle
from tensorflow.keras.models import load_model  # keep only this one

app = FastAPI()

# ----------------------
# CORS Middleware Setup
# ----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins; for production, replace "*" with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # allow all HTTP methods
    allow_headers=["*"],  # allow all headers
)

# ----------------------
# Load artifacts
# ----------------------
model = load_model("house_model.h5", compile=False)
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# ----------------------
# Routes
# ----------------------
@app.get("/")
def home():
    return {"message": "House Price Prediction API is running!"}

@app.post("/predict")
def predict(features: dict):
    # Convert dict → array using saved column order
    try:
        input_data = np.array([features[col] for col in columns]).reshape(1, -1)
    except KeyError as e:
        return {"error": f"Missing feature: {e.args[0]}"}

    # Scale input
    scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(scaled)[0][0]

    return {"predicted_price": float(prediction)}

# ----------------------
# Run server
# ----------------------
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
