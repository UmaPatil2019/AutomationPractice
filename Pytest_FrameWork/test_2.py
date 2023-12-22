import pytest

class TestClass:

    #decorator
    @pytest.fixture()
    def setup(self):
        print("Launching browser...")
        print("Open Application...")
        # yield prints at the end of test methods
        yield
        print("Closing browser....")

    #if setup is called in the test methods, then shows the print statements
    def test_Login(self, setup):
        print("this is Login test")

    def test_Search(self,setup):
        print("this is Search test")

    def test_AdvancedSearch(self):
        print("this is Advanced serach test")