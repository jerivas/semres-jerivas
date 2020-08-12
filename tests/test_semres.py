import pytest

from semres import hello, goodbye


@pytest.mark.parametrize(
    "x,out",
    [
        (0, "Hello world 3! 0"),
        ("mary", "Hello world 3! mary"),
        (None, "Hello world 3! None"),
    ],
)
def test_hello(x, out):
    assert hello(x) == out


@pytest.mark.parametrize(
    "x,out", [("joe", "Goodbye 3 joe"), ("mary", "Goodbye 3 mary")]
)
def test_goodbye(x, out):
    assert goodbye(x) == out
