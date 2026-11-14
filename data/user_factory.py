from faker import Faker

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
    def generate_valid_user():
        user_email = UserFactory.generate_email(),
        user_password = UserFactory.generate_password()

        return {
            "email": user_email,
            "password": user_password,
            "confirm_password": user_password
        }
