import test_variables


def test_one():
    test_variables.test_value = 1
    assert True


def test_two():
    assert test_variables.test_value == 1
