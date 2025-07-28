# DeepWebAi Gelişmiş Yapay Zeka 

Bu proje FastAPI tabanlı bir backend ve React tabanlı bir frontend icerir. 
Basit bir yapay zeka servisinin ornek iskeletini sunar.

## Kurulum

```bash
bash scripts/init_project.sh
```

Backend uygulamasını çalıştırmak için:
```bash
uvicorn backend.app.main:app --reload
```
Frontend ise Vite kullanır.

E2E testleri için [Playwright](https://playwright.dev/) kullanılır. Canlı uygulamanın ekran görüntüsünü almak için:
```bash
cd frontend
npx playwright test
```

