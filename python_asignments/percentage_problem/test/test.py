import unittest
from percentage_problem.core.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualinput=percentage_calculation({'a':[10,20,30],'b':[30,60,40]},'a')
        expectedoutput=20.0
        self.assertEqual( actualinput,expectedoutput)  # add assertion here

    def test_somethin(self):
        actualinput = percentage_calculation({'a': [10, 20, 50], 'b': [30, 60, 40]}, 'a')
        expectedoutput = 26.666666666666668
        self.assertEqual(actualinput, expectedoutput)

if __name__ == '__main__':
    unittest.main()
