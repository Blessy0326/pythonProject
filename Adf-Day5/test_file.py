
import pytest
from exday_five import *
class TestOperations():
    def test_age(self):
        test_1 = Application().validate_age(GENDER_NAME,D_O_B)
        assert test_1 == "Valid" or "Invalid"

    def test_state(self):
        test_1 = Application().validate_state(STATE_NAME)
        assert test_1 == "Valid" or "Invalid"

    def test_salary(self):
        test_1 = Application().validate_salary(SALARY_OF_PERSON)
        assert test_1 == "Valid" or "Invalid"

    def test_nationality(self):
        test_1 = Application().validate_nationality(NATIONALITY_NAME)
        assert test_1 == "Valid" or "Invalid"

    def test_pan(self):
        test_1 = Application().validate_pan(PAN_NUM)
        assert test_1 == "Valid" or "Invalid"