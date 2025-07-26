@echo off
REM ---- Kök dizini bul ----
set "ROOT=%~dp0"
cd /d "%ROOT%"

REM --- Backend Başlat ---
if not exist backend\venv (
    cd backend
    python -m venv venv
    call venv\Scripts\activate
    pip install -r requirements.txt
    cd ..
)

start "Backend" cmd /k "cd /d %ROOT%backend && call venv\Scripts\activate && uvicorn app.main:app --reload"

REM --- Frontend Başlat ---
start "Frontend" cmd /k "cd /d %ROOT%frontend && npm install && npm run dev"

echo Tum servisler baslatildi.
pause
