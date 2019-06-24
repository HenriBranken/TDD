from line_reader import read_from_file
import pytest
from pytest import raises
from unittest.mock import MagicMock

# To Do List:
# (1) Can call read_from_file.
# (2) read_from_file returns the correct string.
# (3) read_from_file throws an exception when the file does not exist.


# Create a test fixture for creating the first set of mocks that are common
# between the two tests
@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()  # Mock the open function to return a MagicMock() object.
    mock_file.readline = MagicMock()  # Add a .readline attribute to the Mock, which is also a MagicMock() object
    mock_file.readline.return_value = "test line"  # MagicMock object will return the test string.

    mock_open = MagicMock(return_value=mock_file)   # Mock the open function to return a MagicMock() object, mock_file
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open


# I don't actually want to open a file for this test though, as that puts an
# external dependency on the test that can potentially slow the test down.
#
# Instead, I will mock out the open function to return a MagicMock object,
# and I'll add a .readline attribute to the Mock, which is also a MagicMock
# object that will return the test string.
#
# Then I will call the read_from_file function, and when that call returns, I
# will validate that the open function was called with the correct parameters,
# and that the expected test string was returned.
def test_returns_correct_string(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)  # Mock the "os.path.exists" functionality so that I can control when it returns True or False depending on the test case.
    monkeypatch.setattr("os.path.exists", mock_exists)

    result = read_from_file("blah")  # Call the read_from_file function.
    mock_open.assert_called_once_with("blah", "r")  # validate that the open function was called with the correct parameters.
    assert result == "test line"  # validate that the expected test string was returned.


# Update the function to throw an exception if the specified file does not
# exist.
#
# Going to assume that the production code will use the os.path.exists
# function to verify whether or not the file exists, and then throw an
# Exception if it does not.
#
# Mock the os.path.exists function so that I can control when it returns True,
# or False depending on the test case, without having to make modifications in
# the actual file system itself.
def test_throws_exception_with_bad_file(monkeypatch):
    mock_exists = MagicMock(return_value=False)  # Mock the "os.path.exists" functionality so that I can control when it returns True or False depending on the test case.
    monkeypatch.setattr("os.path.exists", mock_exists)

    with raises(Exception):
        read_from_file("blah")
