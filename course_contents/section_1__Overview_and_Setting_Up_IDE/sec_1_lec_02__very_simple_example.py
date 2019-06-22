import pytest


# Production Code:  A function that returns the length of a passed-in string.
def str_len(the_string):
    return len(the_string)


# A Unit Test:
# A single, simple positive test case.
def test_string_length():
    # The setup step.  Creates the test string.
    test_string = "a"

    # Action step.  Calls the production code.
    result = str_len(test_string)

    # Assertion step.  Test evaluates the result of the action.
    assert result == 1
