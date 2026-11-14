from playwright.sync_api import Page, Locator


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def fill(self, locator: Locator, text: str):
        locator.fill(text)

    def clear(self, locator: Locator):
        locator.clear()

    def click(self, locator: Locator):
        locator.click()

    def should_be_visible(self):
        pass

    def open(self, path: str):
        self.page.goto(path)




