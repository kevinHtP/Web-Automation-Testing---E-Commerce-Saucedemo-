from playwright.sync_api import sync_playwright

def test_login_gagal():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        print("1. Membuka halaman Saucedemo...")
        page.goto("https://www.saucedemo.com/")

        print("2. Mengisi Username benar dan Password SALAH...")
        page.fill("#user-name", "standard_user")
        # Kita sengaja memasukkan password yang salah di bawah ini
        page.fill("#password", "password_ngasal")

        print("3. Mengklik tombol Login...")
        page.click("#login-button")

        print("4. Melakukan Validasi Error (Assertion)...")
        # Membaca teks error yang muncul di layar
        # Elemen kotak merah di saucedemo memiliki atribut data-test='error'
        pesan_error = page.locator("[data-test='error']").inner_text()
        
        # Memastikan pesan error mengandung kata yang tepat
        assert "do not match" in pesan_error
        
        print(f"Pesan dari sistem: {pesan_error}")
        print("✅ NEGATIVE TEST BERHASIL: Sistem menolak login dan menampilkan error yang benar!")

        browser.close()

if __name__ == "__main__":
    test_login_gagal()