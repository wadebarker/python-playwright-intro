from dataclasses import dataclass


@dataclass
class RegisterUser:
    username: str
    password: str
    confirm_password: str