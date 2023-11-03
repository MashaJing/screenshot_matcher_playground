
import vedro
import playwright
from os import environ

@vedro.context
async def opened_index_page():
    browser = await playwright.chromium.launch()
    page = await browser.new_page()

    await page.goto(environ["APP_URL"])

    return page
