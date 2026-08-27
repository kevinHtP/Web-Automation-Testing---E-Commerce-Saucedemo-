import pytest
from playwright.sync_api import Page

# Skenario 1: Happy Path
def test_login_sukses(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    # Validasi
    assert page.url == "https://www.saucedemo.com/inventory.html"

# Skenario 2: Negative Test
def test_login_gagal(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "password_ngasal")
    page.click("#login-button")
    
    # Validasi
    pesan_error = page.locator("[data-test='error']").inner_text()
    assert "do not match" in pesan_error