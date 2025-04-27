from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
context = browser.new_context()
page = context.new_page()
page.set_viewport_size({"width": 1920, "height": 1080})  # Assuming a common screen resolution

page.goto("https://galmatalon.github.io/tutorials/indexID.html")

first_name = page.locator("#firstname")
last_name = page.locator("#lastname")
email = page.locator("#email")
next_btn = page.locator("#next")

first_name.fill("Boris")
last_name.fill("Sionov")
email.fill("mail@gmail.com")
next_btn.click()

input("end")
