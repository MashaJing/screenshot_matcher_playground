from os import environ
import vedro_playwright as playwright

import vedro
import vedro_screenshot_matcher


class Config(vedro.Config):
    class Plugins(vedro.Config.Plugins):
        class ScreenshotMatcher(vedro_screenshot_matcher.ScreenshotMatcher):
            enabled = True

            golden_app_url = environ.get("APP_URL", "")
            test_app_url = environ.get("TEST_APP_URL", "")

        class Playwright(playwright.Playwright):
            enabled = True
