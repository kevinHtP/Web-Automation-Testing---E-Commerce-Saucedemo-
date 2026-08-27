from playwright.sync_api import sync_playwright

def jalankan_test():
    # Memulai sesi Playwright
    with sync_playwright() as p:
        # headless=False artinya browser akan tampil di layar (tidak jalan diam-diam)
        # slow_mo=500 memberikan jeda 0.5 detik setiap aksi agar kita bisa melihat bot bekerja
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("1. Membuka halaman Saucedemo...")
        page.goto("https://www.saucedemo.com/")

        print("2. Mengisi Username dan Password...")
        # "#user-name" dan "#password" adalah CSS Selector dari kolom input di website tersebut
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        print("3. Mengklik tombol Login...")
        page.click("#login-button")

        print("4. Melakukan Validasi (Assertion)...")
        # Memastikan bot berhasil masuk ke halaman produk
        assert page.url == "https://www.saucedemo.com/inventory.html"
        
        print("✅ TEST BERHASIL: Login sukses dan masuk ke dashboard!")

        # Tutup browser
        browser.close()

if __name__ == "__main__":
    jalankan_test()