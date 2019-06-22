import pytest


@pytest.fixture(scope="module", autouse=True)
def setup_module_2():
    print("\nSetup Module 2")


@pytest.fixture(scope="class", autouse=True)
def setup_class_2():
    print("\nSetup Class 2")


@pytest.fixture(scope="function", autouse=True)
def setup_function_2():
    print("\nSetup Function 2")


class TestClass:
    def test_it_1(self):
        print("Test It 1")
        assert True

    def test_it_2(self):
        print("Test It 2")
        assert True
