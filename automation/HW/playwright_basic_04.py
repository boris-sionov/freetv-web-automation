import time

from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
context = browser.new_context()
page = context.new_page()
page.set_viewport_size({"width": 1920, "height": 1080})
page.set_default_timeout(10000)

# Tested browser link
page.goto("https://login.salesforce.com/")

# Locators on current page
user_name_box = page.locator("#username")
psw_box = page.locator("#password")
remember_me_radio_btn = page.locator("#rememberUn")
login_btn = page.locator("#Login")

# Actions
user_name_box.fill("Boris sionov")
psw_box.fill("qwerty")
remember_me_radio_btn.click()
check_not = remember_me_radio_btn.is_checked()
if check_not is True:
    print(f"The box check is: {check_not}, therefor pressing on login")
    login_btn.click()
else:
    print(f"The box check is: {check_not}, Unable to click on Login closing the session")
time.sleep(4)
