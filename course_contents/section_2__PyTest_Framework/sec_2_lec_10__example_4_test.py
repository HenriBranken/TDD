import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_session():
    print("\nSetup Session")


@pytest.fixture(scope="module", autouse=True)
def setup_module():
    print("\nSetup Module")


@pytest.fixture(scope="function", autouse=True)
def setup_function():
    print("\nSetup Function")


def test_1():
    print("Executing Test 1")
    assert True


def test_2():
    print("Executing Test 2")
    assert True
