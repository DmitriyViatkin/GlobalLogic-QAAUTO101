import pytest


def test_change_name(user):
    assert user.name == "Djon"


@pytest.mark.check
def test_chsnge_second_name(user):
    assert user.second_name == "Dou"
