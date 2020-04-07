import pytest

from semres import hello, goodbye


@pytest.mark.parametrize(
    "input,expected",
    [(0, "Hello world! 0"), ("mary", "Hello world! mary"), (None, "Hello world! None")],
)
def test_hello(input, expected):
    assert hello(input) == expected


@pytest.mark.parametrize(
    "input,expected", [("joe", "Goodbye joe"), ("mary", "Goodbye mary")]
)
def test_goodbye(input, expected):
    assert goodbye(input) == expected
