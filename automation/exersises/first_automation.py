from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])


page = browser.new_page()
page.set_viewport_size({"width": 1920, "height": 1080})  # Assuming a common screen resolution

page.goto("https://playwright.dev/python/")
input("end")
