# frontend/app.py
import streamlit as st
import requests

API_URL = "http://localhost:8000"  # Your FastAPI base URL

st.set_page_config(page_title="Fraud Detection System", layout="centered")
st.title("🔍 AI/ML Fraud Detection System")
st.markdown("Detect fraudulent websites and fake reviews using AI")

# --- URL Fraud Detection ---
st.header("🌐 URL Fraud Checker")
url_input = st.text_input("Enter website URL")

if st.button("Check URL"):
    if url_input:
        response = requests.post(f"{API_URL}/predict_url", json={"url": url_input})
        if response.ok:
            result = response.json()
            st.success("✅ Safe URL" if not result["is_fraud"] else "⚠️ Fraudulent URL Detected!")
            st.json(result)
        else:
            st.error("API Error while checking URL")

# --- Fake Review Detection ---
st.header("📝 Review Analyzer")
review_input = st.text_area("Paste a review")

if st.button("Analyze Review"):
    if review_input:
        response = requests.post(f"{API_URL}/predict_review", json={"review": review_input})
        if response.ok:
            result = response.json()
            st.success("✅ Real Review" if not result["is_fake"] else "🚨 Fake Review Detected!")
            st.json(result)
        else:
            st.error("API Error while checking review")
