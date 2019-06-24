from unittest.mock import MagicMock
from my_abc import AbstractAdder, ConcreteAdder, AddExecuter

# This lecture is a walkthrough of mocking out a concrete instantiation of an
# abstract interface.
#
# How to use MagicMock to create a mock of an abstract base class for testing
# a function that uses that abstract base class in my production.
#
# To do:
# - Can all AddExecuter
# - AddExecuter calls AbstractAdder properly and returns the correct result.


# Creating a mock AbstractAdder instance with a Mock of the add method, then
# I'll pass that into a call to the AddExecuter.
# Then I can use the AddMock to verify it was called correctly, and verify the
# response from the AddExecutor.
def test_AddExecuter_call_and_returns():
    mock_adder = MagicMock(AbstractAdder)
    mock_adder.add = MagicMock(return_value=3)
    result = AddExecuter(mock_adder)
    mock_adder.add.assert_called_once_with(1, 2)
    assert result == 3
