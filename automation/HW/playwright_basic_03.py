import time

from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.chromium.launch(headless=False, slow_mo=1000, args=["--start-maximized"])
context = browser.new_context()
page = context.new_page()
page.set_viewport_size({"width": 1920, "height": 1080})
page.set_default_timeout(10000)


page.goto("http://www.ebay.com/sch/ebayadvsearch")

enter_box = page.locator("#_nkw")
enter_box.fill("tent")
exclude_word_box = page.locator("#_ex_kw")
exclude_word_box.fill("giant")
buy_it_now = page.locator('text="Buy It Now"')
buy_it_now.click()
search_bottom = page.locator(".adv-form__actions > button")
search_bottom.click()
time.sleep(1)
page.go_back()
time.sleep(5)

