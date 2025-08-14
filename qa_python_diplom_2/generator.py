import random
import string


class Generator:

    @staticmethod
    def email_generate(length):
        letters = string.ascii_lowercase
        random_email = ''.join(random.choice(letters) for i in range(length))
        return f'{random_email}{"@yandex.ru"}'

    @staticmethod
    def password_generate(length):
        letters = string.ascii_lowercase
        random_password = ''.join(random.choice(letters) for i in range(length))
        return random_password

    @staticmethod
    def name_generate(length):
        letters = string.ascii_lowercase
        random_name = ''.join(random.choice(letters) for i in range(length))
        return random_name
