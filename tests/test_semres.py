import pytest

from semres import hello, goodbye, my_yesno


@pytest.mark.parametrize(
    "x,out",
    [
        (0, "Hello world 4! 0"),
        ("mary", "Hello world 4! mary"),
        (None, "Hello world 4! None"),
    ],
)
def test_hello(x, out):
    assert hello(x) == out


@pytest.mark.parametrize(
    "x,out", [("joe", "Goodbye 4 joe"), ("mary", "Goodbye 4 mary")]
)
def test_goodbye(x, out):
    assert goodbye(x) == out


@pytest.mark.parametrize(
    "x,y,out",
    [
        (True, "", True),
        (False, "", False),
        (True, "yay,nay", "yay"),
        (False, "yay,nay", "nay"),
    ],
)
def test_yesno(x, y, out):
    assert my_yesno(x, y) == out
