# 🤖 Web Automation Testing - E-Commerce (Saucedemo)

Proyek ini adalah portofolio pengujian otomasi *End-to-End* (E2E) untuk sebuah *website* *e-commerce*. Proyek ini dibangun untuk memastikan alur logika sistem bekerja dengan baik dan mendemonstrasikan implementasi pengujian otomatis terstruktur.

## 🛠️ Teknologi yang Digunakan
*   **Bahasa Pemrograman:** Python
*   **Automation Tool:** Playwright
*   **Testing Framework:** Pytest
*   **Reporting:** pytest-html

## 📋 Skenario Pengujian (Test Cases)
*   **Authentication:** Menguji validasi *login* sukses (*positive test*) dan penolakan akses saat *password* salah (*negative test*).
*   **Product Flow:** Memastikan fungsionalitas keranjang belanja.
*   **Checkout E2E:** Mengotomatisasi pengisian data diri hingga konfirmasi pesanan berhasil.
*   **Error Handling:** Sistem otomatis mengambil tangkapan layar (*screenshot*) saat terjadi kegagalan skenario.

## 🚀 Cara Menjalankan Project Secara Lokal
1.  Kloning repositori ini ke komputer Anda.
2.  Install library yang dibutuhkan: `pip install pytest-playwright pytest-html`
3.  Install engine browser: `playwright install`
4.  Jalankan perintah pengujian: `pytest --html=report.html --self-contained-html`

## 📊 Contoh Laporan (Reporting)
Proyek ini secara otomatis menghasilkan laporan HTML yang rapi beserta bukti visual jika ada *error*.


page = <Page url='https://www.saucedemo.com/inventory.html'>

    def test_checkout_barang_sukses(page):
        # 1. Login (Sama seperti sebelumnya)
        print("Membuka halaman login...")
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
    
        # Pastikan berhasil masuk
>       assert page.url == "https://www.saucedemo.com/inventory.htmly"
E       AssertionError: assert 'https://www....nventory.html' == 'https://www....ventory.htmly'
E         
E         - https://www.saucedemo.com/inventory.htmly
E         ?                                         -
E         + https://www.saucedemo.com/inventory.html

test_checkout.py:12: AssertionError

----------------------------- Captured stdout call -----------------------------
Membuka halaman login...
