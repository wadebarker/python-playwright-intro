from faker import Faker

from models import RegisterUser

fake = Faker()


class UserFactory:

    @staticmethod
    def generate_email() -> str:
        return fake.email()


    @staticmethod
    def generate_password() -> str:
        return fake.password(
            length=10,
            digits=True,
            upper_case=True,
            lower_case=True
        )


    @staticmethod
    def generate_valid_user() -> RegisterUser:
        password = UserFactory.generate_password()

        return RegisterUser(
            email=UserFactory.generate_email(),
            password=password,
            confirm_password=password
        )
