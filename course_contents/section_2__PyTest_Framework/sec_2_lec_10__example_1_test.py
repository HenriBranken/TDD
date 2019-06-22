import pytest


@pytest.fixture()
def setup():
    print("\nSetup")


def test_1(setup):
    # setup() is called before test_1 executes.
    print("Executing test 1.")
    assert True


@pytest.mark.usefixtures("setup")
# setup() will be called before test_2 executes.
# This is just an alternative to specifying:
# def test_2(setup):
def test_2():
    print("Executing test 2.")
    assert True
