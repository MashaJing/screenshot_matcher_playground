import vedro
import screenshot_matcher


class Config(vedro.Config):
    class Plugins(vedro.Config.Plugins):
        class ScreenshotMatcher(screenshot_matcher.ScreenshotMatcher):
            test_app_url = "http://localhost"
            golden_app_url = "http://golden-app.com"
