#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy pydantic
if [ -f "backend/requirements.txt" ]; then
    pip install -r backend/requirements.txt
fi
if [ -f "frontend/package.json" ]; then
    cd frontend
    npm install || echo "Frontend kurulumu için package.json eksik/hatalı."
    cd ..
fi
echo "Kurulum tamamlandı."

