from os import environ
from pathlib import Path

import vedro
import screenshot_matcher


class Config(vedro.Config):
    class Plugins(vedro.Config.Plugins):
        class ScreenshotMatcher(screenshot_matcher.ScreenshotMatcher):
            enabled = True
            screenshots_dir = Path("./snapshots")

            golden_app_url = environ.get("APP_URL", "")
            test_app_url = environ.get("TEST_APP_URL", "")
