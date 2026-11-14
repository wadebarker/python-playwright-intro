from dataclasses import dataclass


@dataclass
class RegisterUser:
    email: str
    password: str
    confirm_password: str