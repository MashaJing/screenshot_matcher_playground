import vedro
from screenshot_matcher import screenshot_asserts, match_screenshot
from contexts import opened_index_page


@screenshot_asserts()  # Step 1: Add decorator
class Scenario(vedro.Scenario):
    subject = "share page"

    def given_opened_page(self):
        self.page = opened_index_page()

    def when_user_click_on_share(self):
        self.page.get_by_text("Share").click()

    def then_it_should_show_share_popup(self):
        share_popup = self.page.locator(".share-popup .title")
        assert share_popup.text_content() == "Share Page"
        assert match_screenshot(share_popup)  # Step 2: Add screenshot assertion
