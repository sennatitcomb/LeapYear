import unittest
import cs362hw1

class testCaseLeapYear(unittest.TestCase):
    def test_1(self):
        result = cs362hw1("2000")
        self.assertEqual(result,"This is not a leap year")
    def test_2(self):
       result = cs362hw1("2021")
       self.assertEqual(result,"This is a leap year")

if __name__ == '__main__':
    unittest.main();