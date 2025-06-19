# run.sh

#!/bin/bash

echo "🚀 Starting Fraud Detection System..."

# Activate your virtual environment if needed
# source venv/bin/activate

# Start FastAPI backend
echo "✅ Starting FastAPI backend..."
cd backend
uvicorn main:app --reload &
BACKEND_PID=$!
cd ..

# Wait a moment for backend to start
sleep 3

# Start Streamlit frontend
echo "✅ Launching Streamlit frontend..."
cd frontend
streamlit run app.py

# When Streamlit exits, kill the backend
kill $BACKEND_PID
