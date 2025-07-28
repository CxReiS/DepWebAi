import { test } from '@playwright/test';

// Basit ekran görüntüsü testi

test('ana sayfa goruntulensin', async ({ page }) => {
  await page.goto('/');
  await page.screenshot({ path: 'playwright-report/home.png', fullPage: true });
});
