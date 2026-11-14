from tests.base_test import BaseTest


class RegisterPage(BaseTest):
    def test_success_registration(self, user_data):

        self.register_page.register(
            email=user_data['email'],
            password=user_data['password'],
            confirm_password=user_data['password']
        )

        self.register_page.should_be_registered()

