import pytest


class Testclass:

    @pytest.mark.sanity
    def test_LoginByEmail(self, setup):
        print("this is login by email...")
        assert True == True

    @pytest.mark.sanity
    def test_Login_ByFaceBook(self, setup):
        print("this is login by facebbok...")
        assert True == True

    @pytest.mark.regression
    def test_Login_ByTwitter(self):
        print("this is login by Twitter...")
        assert True == True

    @pytest.mark.regression
    def test_SignUpByEmail(self, setup):
        print("this is signup by email...")
        assert True == True

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SignUP_ByFaceBook(self, setup):
        print("this is signup by facebbok...")
        assert True == True

    @pytest.mark.sanity
    @pytest.mark.regression# skips the testcase
    def test_SignUP_ByTwitter(self):
        print("this is signup by Twitter...")
        assert True == True

