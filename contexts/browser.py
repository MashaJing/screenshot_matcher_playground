
import vedro
from vedro_playwright import BrowserEngine
from vedro_playwright import opened_browser as opened_local_browser
from os import environ

@vedro.context
async def opened_index_page():
    browser = await opened_local_browser(BrowserEngine.CHROMIUM, options={"headless": False})
    page = await browser.new_page()

    await page.goto("file://" + environ["APP_URL"])

    return page
