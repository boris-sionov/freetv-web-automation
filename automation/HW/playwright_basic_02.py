from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
context = browser.new_context()
page = context.new_page()
page.set_viewport_size({"width": 1920, "height": 1080})  # Assuming a common screen resolution

page.goto("https://login.salesforce.com/")

forgot_psw = page.locator("#forgot_password_link")
forgot_psw.click()
title = page.title()
print(f"page title is: {title}")


if "forgot your password" in title.lower():
    user_name = page.locator("#un")
    user_name.fill("My name")
    continue_btn = page.locator("#continue")
    continue_btn.click()
    error_msg = page.locator(".mb16.error")
    error_msg_text = error_msg.inner_text()
    print(f"The error message text is: {error_msg_text}")
else:
    print("no")

