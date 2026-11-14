import pytest

from pages.register_page import RegisterPage

@pytest.mark.usefixtures("register_page")
class BaseTest:

    register_page: RegisterPage

    @pytest.fixture(autouse=True)
    def setup_page(self, register_page):
        self.register_page = register_page