import pytest

#approach1 for oredering
#pytest.ini file should be created first with the keywords like first, seconf, third etc
#use those markers in the python file for the methods
#pytest-ordering package should be installed

# class TestClass:
#
#     @pytest.mark.third
#     def test_methodA(self):
#         print("Running method A....")
#
#     def test_methodB(self):
#         print("Running method B....")
#
#     @pytest.mark.second
#     def test_methodC(self):
#         print("Running method C....")
#
#     def test_methodD(self):
#         print("Running method D....")
#
#     @pytest.mark.first
#     def test_methodE(self):
#         print("Running method E....")
#

#second approach
#Ordering can be controlled with @pytest.mark.run(order=any number)
class TestClass:

    @pytest.mark.run(order=5)
    def test_methodA(self):
        print("Running method A....")

    @pytest.mark.run(order=4)
    def test_methodB(self):
        print("Running method B....")

    @pytest.mark.run(order=3)
    def test_methodC(self):
        print("Running method C....")


    @pytest.mark.run(order=2)
    def test_methodD(self):
        print("Running method D....")

    @pytest.mark.run(order=1)
    def test_methodE(self):
        print("Running method E....")