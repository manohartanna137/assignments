import unittest
from calendar_problem.core.utils import*
import datetime



class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualinput= weekday(12,2, 2023)
        expectedoutput="SATURDAY"
        self.assertEqual(actualinput,expectedoutput)  # add assertion here

if __name__ == '__main__':
    unittest.main()
