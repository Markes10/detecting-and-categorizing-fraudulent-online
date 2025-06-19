# backend/utils/predict_url.py
import joblib
import re

model = joblib.load("models/phishing_model.pkl")

def extract_url_features(url: str):
    return [
        1 if "https" not in url else 0,
        1 if re.search(r"\d{2,}", url) else 0,
        1 if "@" in url else 0,
        len(url)
    ]

def predict_url_fraud(url: str):
    features = extract_url_features(url)
    pred = model.predict([features])[0]
    return {"url": url, "is_fraud": bool(pred), "features": features}
