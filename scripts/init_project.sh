#!/bin/bash
# Proje kurulum scripti

python -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt

cd frontend && npm install
