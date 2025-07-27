@echo off
echo === DeepWebAi Kurulum Baslatiliyor ===
set "SECRET_KEY_FILE=D:\Python_Gereksinimleri\Venvler\secrets\deepseek.key"

REM Python ve pip kontrolü
where python >nul 2>nul || (echo Python bulunamadi & exit /b 1)
where pip >nul 2>nul || (echo pip bulunamadi & exit /b 1)

REM Sanal ortam kontrol/kurulum
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate

REM Python bağımlılıkları
echo Python bagimliliklari kuruluyor
pip install --upgrade pip
pip install -r backend\requirements.txt
pip install bandit pip-audit

REM npm kontrol ve frontend kurulumu
where npm >nul 2>nul
if %errorlevel%==0 (
    echo Frontend bagimliliklari kuruluyor
    cd frontend
    npm install
    cd ..
) else (
    echo npm bulunamadi, frontend kurulumu atlandi
)

REM .env dosyası kontrolü
if not exist .env (
    if exist .env.example copy .env.example .env
)

REM SQLAlchemy ile tablo oluşturma (doğrudan python kodu çalıştırmak için)
python -c "from app.database.session import Base, engine; Base.metadata.create_all(bind=engine)"

REM Güvenlik taramasi ve testler
bandit -r backend\app -n 5
pip-audit -r backend\requirements.txt --no-deps
pytest -q

echo Kurulum tamamlandi!
pause
