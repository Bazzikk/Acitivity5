import unittest
import leapYear


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapYear.leapYear("T"),False)

    def test2(self):
        self.assertEqual(leapYear.leapYear(),False)

    def test3(self):
        self.assertEqual(leapYear.leapYear(2),False)

    def test4(self):
        self.assertEqual(leapYear.leapYear(-2),False)

if __name__ == '__main__':
    unittest.main(verbosity = 2)
