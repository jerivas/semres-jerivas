import pytest

from semres import hello, goodbye


@pytest.mark.parametrize(
    "x,out",
    [
        (0, "Hello world 2! 0"),
        ("mary", "Hello world 2! mary"),
        (None, "Hello world 2! None"),
    ],
)
def test_hello(x, out):
    assert hello(x) == out


@pytest.mark.parametrize("x,out", [("joe", "Goodbye joe"), ("mary", "Goodbye mary")])
def test_goodbye(x, out):
    assert goodbye(x) == out
