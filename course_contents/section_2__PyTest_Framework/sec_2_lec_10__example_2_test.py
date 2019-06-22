import pytest


@pytest.fixture(autouse=True)
# Therefore, automatically execute this fixture before each unit test, in this
# fixture scope, is executed.
def setup():
    print("\nSetup")


def test_1():
    print("Executing test 1.")
    assert True


def test_2():
    print("Executing test 2.")
    assert True
