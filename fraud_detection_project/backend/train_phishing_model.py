# backend/train_phishing_model.py
import joblib
from sklearn.ensemble import RandomForestClassifier

# Sample dummy training data (you can replace with real dataset later)
urls = [
    "http://login.example.com@phish.com",
    "https://secure.bankofamerica.com",
    "http://198.51.100.1/login",
    "http://paypal.com.secure-login.tk",
    "https://github.com/login"
]

X = []
y = [1, 0, 1, 1, 0]  # 1 = phishing, 0 = safe

def extract_url_features(url):
    return [
        1 if "https" not in url else 0,
        1 if any(char.isdigit() for char in url) else 0,
        1 if "@" in url else 0,
        len(url)
    ]

for url in urls:
    X.append(extract_url_features(url))

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "models/phishing_model.pkl")
print("✅ Phishing model trained and saved!")
