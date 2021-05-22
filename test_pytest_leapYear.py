import pytest
import leapYear
class TestClass:
    def test_one(self):
        x = "4"
        with pytest.raises(AssertionError):
            assert leapYear.leapYear(x) == False

    def test_two(self):
        assert leapYear.leapYear() == False

    def test_three(self):
        assert leapYear.leapYear(2016) == True

    def test_four(self):
        assert leapYear.leapYear(-2017) == False
