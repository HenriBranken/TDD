class TestClass:
    # has "Test" at the beginning of the class name.
    def test_me(self):
        # automatically discovered by pytest
        assert True

    def test_me2(self):
        # automatically discovered by pytest
        assert True


class MyTestClass:
    # does not have "Test" at the beginning of the class name.
    # Therefore both test_it, and test_it2 are ignored by pytest.
    def test_it(self):
        # ignored by pytest
        assert True

    def test_it2(self):
        # ignored by pytest
        assert True
