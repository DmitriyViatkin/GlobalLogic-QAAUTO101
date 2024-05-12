import pytest


class User:

    def __init__(self, name=None, second_name=None):

        self.name = name
        self.second_name = second_name

    def create_user(self):

        self.name = "Djon"
        self.second_name = "Dou"

    def remove_user(self):

        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():

    user = User()
    user.create_user()
    yield user
    user.remove_user()
