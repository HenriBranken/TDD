class TestClass:
    @classmethod
    # A method that is bound to a class rather than its object.
    # It does not require the creation of a class instance (much like
    # staticmethod).
    # They are passed in the un-instantiated class object, rather than the
    # unique instance of the class.
    def setup_class(cls):
        # Executed by pytest before any of the unit tests in the class are
        # executed.
        print("Setup TestClass!")

    @classmethod
    def teardown_class(cls):
        # This will be executed by pytest after all of the unit tests in the
        # class have executed.
        print("Teardown TestClass!")

    def setup_method(self, function):
        # executed before each unit test in the class is executed.
        if function == self.test1:
            print("\nSetting up test1!")
        elif function == self.test2:
            print("\nSetting upt test2!")
        else:
            print("\nSetting up unknown test!")

    def teardown_method(self, function):
        # executed after each unit test in the class has finished execution.
        if function == self.test1:
            print("\nTearing down test1!")
        elif function == self.test2:
            print("\nTearing down test2!")
        else:
            print("\nTearing down unknown test!")

    def test1(self):
        print("Executing Test1!")
        assert True

    def test2(self):
        print("Executing Test2!")
        assert True
