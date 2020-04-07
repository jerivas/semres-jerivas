import pytest

from semres import hello, goodbye


def test_hello():
    assert hello() == "Hello world!"


@pytest.mark.parametrize(
    "input,expected", [("joe", "Goodbye joe"), ("mary", "Goodbye mary")]
)
def test_goodbye(input, expected):
    assert goodbye(input) == expected
