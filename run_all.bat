@echo off
REM Proje kök dizini: D:\Python_Gereksinimleri\Venvler\DeepWebAi

REM --- Backend Kurulum ve Çalıştırma ---
cd /d D:\Python_Gereksinimleri\Venvler\DeepWebAi\backend
if not exist venv (
    python -m venv venv
    call venv\Scripts\activate
    pip install -r requirements.txt
)
start "Backend" cmd /k "cd /d D:\Python_Gereksinimleri\Venvler\DeepWebAi\backend && call venv\Scripts\activate && uvicorn app.main:app --reload"

REM --- Frontend Kurulum ve Çalıştırma ---
cd /d D:\Python_Gereksinimleri\Venvler\DeepWebAi\frontend
start "Frontend" cmd /k "cd /d D:\Python_Gereksinimleri\Venvler\DeepWebAi\frontend && npm install && npm run dev"

echo Tum servisler baslatildi.
pause
