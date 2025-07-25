#!/bin/bash
# Proje kurulum scripti

python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
pip install fastapi uvicorn sqlalchemy pydantic

cd frontend && npm install

