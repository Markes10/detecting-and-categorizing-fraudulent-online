# backend/train_review_model.py
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample fake vs real reviews
reviews = [
    "Amazing product, must buy!",
    "Totally fake app, doesn't work at all",
    "Works fine, satisfied",
    "This is a scam, they stole my money",
    "Good service and app quality",
    "Fake review, this is a lie",
]
labels = [0, 1, 0, 1, 0, 1]  # 1 = fake, 0 = real

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)

model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "models/review_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")
print("✅ Review model and vectorizer saved!")
