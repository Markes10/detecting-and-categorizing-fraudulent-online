# backend/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from utils.predict_url import predict_url_fraud
from utils.predict_review import predict_review_fraud

app = FastAPI()

# Enable CORS (for Streamlit frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Fraud Detection API running"}

@app.post("/predict_url")
async def predict_url(data: dict):
    url = data.get("url", "")
    prediction = predict_url_fraud(url)
    return prediction

@app.post("/predict_review")
async def predict_review(data: dict):
    review = data.get("review", "")
    prediction = predict_review_fraud(review)
    return prediction
