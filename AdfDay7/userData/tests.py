import unittest
from .validation import Check_eligibity


# Create your tests here.
class TestUser(unittest.TestCase):
        def test_valid(self):
                res = Check_eligibity("male","1993-07-04","indian","karnataka","23454")
                assert res == '{"Response": "Valid"}'
        def test_invalid_nationationality(self):
                res = Check_eligibity("male","1993-07-04","canadian","karnataka","23454")
                assert res == '{"Response": "Invalid nationality"}'
        def test_invalid_state(self):
                res = Check_eligibity("male","1993-07-04","indian","kerala","23454")
                assert res == '{"Response": "Invalid state"}'
        def test_invalid_dob(self):
                res = Check_eligibity("male","2001-07-04","indian","karnataka","23454")
                assert res == '{"Response": "Invalid age"}'
        def test_invalid_female(self):
                res = Check_eligibity("female", "2017-07-03", "indian", "karnataka", "23454")
                assert res == '{"Response": "Invalid age"}'
        def test_valid_female(self):
                res = Check_eligibity("female", "1995-07-03", "indian", "karnataka", "23454")
                assert res == '{"Response": "Valid"}'
        def test_invalid_salary(self):
                res = Check_eligibity("male","1993-07-04","indian","karnataka","1234")
                assert res == '{"Response": "Invalid salary"}'







