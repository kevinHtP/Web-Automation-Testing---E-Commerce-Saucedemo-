import pytest
import base64

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Memanggil plugin pytest-html
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # Mengecek apakah tes sedang berada di fase eksekusi (call)
    if report.when == "call":
        # Mengecek apakah tes tersebut GAGAL
        if report.failed:
            # Mengambil kontrol browser (fixture 'page') dari tes yang gagal
            page = item.funcargs.get("page")
            if page:
                # Mengambil screenshot dan menyimpannya ke memori (bytes)
                screenshot_bytes = page.screenshot()
                
                # Mengubah gambar menjadi format base64 agar bisa masuk ke HTML
                encoded_image = base64.b64encode(screenshot_bytes).decode('utf-8')
                
                # Membuat elemen gambar HTML (bisa diklik untuk memperbesar)
                html_img = f'''
                    <div>
                        <img src="data:image/png;base64,{encoded_image}" alt="screenshot" 
                             style="width:400px; height:auto; border: 1px solid #ccc; cursor: pointer;" 
                             onclick="window.open(this.src)"/>
                        <p style="color: red;"><b>📸 Screenshot saat error:</b></p>
                    </div>
                '''
                # Memasukkan gambar ke dalam laporan tambahan (extra)
                extra.append(pytest_html.extras.html(html_img))
        
        report.extra = extra