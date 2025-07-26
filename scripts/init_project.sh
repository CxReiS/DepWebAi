#!/bin/bash
# Basit kurulum: sanal ortam ve paket kurulumu
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt 2>/dev/null || echo "Gerekli paket dosyasi yok"
echo "Proje hazir"

