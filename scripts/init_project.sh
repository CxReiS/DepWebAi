#!/bin/bash
# Basit kurulum: sanal ortam ve paket kurulumu
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
if [ -f "backend/requirements.txt" ]; then
    pip install -r backend/requirements.txt
fi
echo "Proje hazir"

