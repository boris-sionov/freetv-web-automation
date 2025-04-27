from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
context = browser.new_context()
page = context.new_page()
page.set_viewport_size({"width": 1920, "height": 1080})  # Assuming a common screen resolution

page.goto("https://prd.canvusapps.com/signup")

page.locator("#user_name").fill("Boris")
page.locator("#user_email").fill("email@mail.com")
page.locator("#user_password").fill("PsW112233")
page.locator("#user_password_confirmation").fill("PsW1122331")
page.locator("#company_name").fill("The Best company in the hole world")
page.locator(".submit.btn.btn-primary").click()

error_text = page.locator(".alert.alert-error.alert-block.error").inner_text()
print(f"The text of the error is: {error_text}")

# input("end")
