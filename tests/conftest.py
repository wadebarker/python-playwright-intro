import pytest
from playwright.sync_api import Page

from config.setting import DEFAULT_TIMEOUT
from data.user_factory import UserFactory
from pages.register_page import RegisterPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }


@pytest.fixture
def register_page(page: Page):
    register_page = RegisterPage(page)
    register_page.open_register_page()
    return register_page


@pytest.fixture
def user_data():
    return UserFactory.generate_valid_user()