from unittest.mock import MagicMock
from network_mock import get_url

# To-do list for test_network_mock.py:
# 1. Can call get_url
# 2. get_url calls HTTP correct and returns the correct response.


# Use mokeypatch and MagicMock to create a mock instance of the requests
# library get function call.
#
# Then I'll create another mock object for the return result object
def test_calls_https_correctly_and_returns_correct_response(monkeypatch):
    mock_result = MagicMock()
    mock_result.text = "Hello World!"

    mock_get = MagicMock(return_value=mock_result)
    monkeypatch.setattr("requests.get", mock_get)

    result = get_url("http://www.cnn.com")
    mock_get.assert_called_once_with("http://www.cnn.com")

    assert result.text == "Hello World!"


# Next Lecture Video Course:
# - Update the checkout cart class to read prices from a file and implement my
# unit tests by mocking out the file system.
