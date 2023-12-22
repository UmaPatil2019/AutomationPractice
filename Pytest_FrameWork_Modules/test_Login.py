import pytest

class TestLogin:
    def test_LoginByEmail(self,setup):
        print("this is login by email...")
        assert True==True

    def test_Login_ByFaceBook(self,setup):
        print("this is login by facebbok...")
        assert True == True

    def test_Login_ByTwitter(self):
        print("this is login by Twitter...")
        assert True == True
