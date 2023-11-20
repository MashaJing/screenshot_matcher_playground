from os import environ
from pathlib import Path
import vedro_playwright as playwright

import vedro
import vedro_screenshot_matcher


class Config(vedro.Config):
    class Plugins(vedro.Config.Plugins):
        class ScreenshotMatcher(vedro_screenshot_matcher.ScreenshotMatcher):
            enabled = True
            screenshots_dir = Path("./snapshots")

            golden_app_url = environ.get("APP_URL", "")
            test_app_url = environ.get("TEST_APP_URL", "")

        class Playwright(playwright.Playwright):
            enabled = True
