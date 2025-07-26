#!/usr/bin/env bash
set -e

echo "=== DeepWebAi Kurulum Baslatiliyor ==="

if ! command -v python3 >/dev/null 2>&1; then
    echo "Python3 bulunamadi" >&2
    exit 1
fi

if ! command -v pip >/dev/null 2>&1; then
    echo "pip bulunamadi" >&2
    exit 1
fi

if [ ! -d venv ]; then
    python3 -m venv venv
fi
source venv/bin/activate
export PYTHONPATH="$PWD/backend"

echo "Python bagimliliklari kuruluyor"
pip install --upgrade pip
pip install -r backend/requirements.txt
pip install bandit pip-audit

if command -v npm >/dev/null 2>&1; then
    echo "Frontend bagimliliklari kuruluyor"
    (cd frontend && npm install)
else
    echo "npm bulunamadi, frontend kurulumu atlandi" >&2
fi

if [ ! -s .env ] && [ -f .env.example ]; then
    cp .env.example .env
fi

echo "Veritabani tablolari olusturuluyor"
python <<'EOF'
from app.database.session import Base, engine
Base.metadata.create_all(bind=engine)
EOF

echo "Guvenlik taramasi ve testler calistiriliyor"
bandit -r backend/app -n 5
pip-audit -r backend/requirements.txt --no-deps
pytest -q

echo "Kurulum tamamlandi"

