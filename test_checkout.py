import pytest

def test_checkout_barang_sukses(page):
    # 1. Login (Sama seperti sebelumnya)
    print("Membuka halaman login...")
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # Pastikan berhasil masuk
    assert page.url == "https://www.saucedemo.com/inventory.html"

    # 2. Tambah Barang ke Keranjang
    print("Menambahkan 'Sauce Labs Backpack' ke keranjang...")
    # Tombol add-to-cart punya ID unik berdasarkan nama barang
    page.click("#add-to-cart-sauce-labs-backpack")
    
    # 3. Masuk ke Keranjang
    print("Membuka keranjang belanja...")
    # Ikon keranjang memiliki class .shopping_cart_link
    page.click(".shopping_cart_link")
    # Validasi: URL harus mengandung tulisan "cart"
    assert "cart.html" in page.url

    # 4. Mulai Checkout
    print("Memulai proses checkout...")
    page.click("#checkout")

    # 5. MENGISI FORMULIR DATA DIRI
    print("Mengisi formulir checkout...")
    page.fill("#first-name", "John")
    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "12345")
    
    # Klik tombol lanjut
    page.click("#continue")

    # 6. Halaman Ringkasan (Overview)
    print("Mereview pesanan...")
    # Validasi: Memastikan kita masuk ke halaman overview
    assert "checkout-step-two.html" in page.url
    
    # Opsional: Memastikan total barang sesuai (ada elemen div dengan nama class 'cart_item')
    jumlah_barang = page.locator(".cart_item").count()
    assert jumlah_barang == 1

    # 7. Selesaikan Pesanan
    print("Menyelesaikan pesanan...")
    page.click("#finish")

    # 8. Validasi Berhasil (Tulisan 'Thank you for your order!')
    print("Validasi pesanan sukses...")
    teks_sukses = page.locator(".complete-header").inner_text()
    assert teks_sukses == "Thank you for your order!"