
import joblib

model = joblib.load("models/review_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_review_fraud(review: str):
    X = vectorizer.transform([review])
    pred = model.predict(X)[0]
    return {"review": review, "is_fake": bool(pred)}
