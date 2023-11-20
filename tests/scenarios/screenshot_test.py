import vedro
from vedro_screenshot_matcher import screenshot_asserts, match_screenshot
from contexts import opened_index_page


@screenshot_asserts()  # Step 1: Add decorator
class Scenario(vedro.Scenario):
    subject = "open main page"

    async def when_user_opens_main_page(self):
        self.page = await opened_index_page()

    async def then_it_should_show_content(self):
        self.main_block = self.page.locator("main-content")
        assert await match_screenshot(self.main_block)  # Step 2: Add screenshot assertion
