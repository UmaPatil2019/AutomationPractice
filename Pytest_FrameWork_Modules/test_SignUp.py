import pytest


class TestSignUP:
    def test_SignUpByEmail(self, setup):
        print("this is signup by email...")
        assert True == True

    def test_SignUP_ByFaceBook(self, setup):
        print("this is signup by facebbok...")
        assert True == True


    @pytest.mark.skip #skips the testcase
    def test_SignUP_ByTwitter(self):
        print("this is signup by Twitter...")
        assert True == True
