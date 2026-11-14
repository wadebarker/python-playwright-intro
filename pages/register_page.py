from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.form = page.locator(".Register_form__grV82")
        self.email_input = page.locator("input[name='email']")
        self.password_input = page.locator("input[name='password']")
        self.confirm_password_input = page.locator("input[name='repeat']")
        self.register_button = page.locator("form button[type='submit']")
        self.clear_button = page.locator("form button[type='reset']")

    def open_register_page(self):
        self.open("/auth/register")
        expect(self.form).to_be_visible()
        return self

    def enter_email(self, email: str):
        self.fill(self.email_input, email)
        return self

    def enter_password(self, password: str):
        self.fill(self.password_input, password)
        return self

    def enter_confirm_password(self, password: str):
        self.fill(self.confirm_password_input, password)
        return self

    def fill_registration_form(self, email: str, password: str, confirm_password: str):
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        return self

    def click_register(self):
        self.click(self.register_button)
        return self

    def click_reset(self):
        self.click(self.clear_button)
        return self

    def register(self, email: str, password: str, confirm_password: str):
        self.fill_registration_form(email, password, confirm_password)
        self.click_register()
        return self

    def should_be_registered(self, page: Page):
        expect(page).toHaveURL('/')