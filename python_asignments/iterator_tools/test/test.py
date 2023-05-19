import unittest
from iterator_tools.core.utils import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        size=4
        input=['a','a','c','d']
        k=2
        actualinput= iterables(size,input,k)
        expectedoutput= '0.833'
        self.assertEqual(actualinput, expectedoutput)  # add assertion here


if __name__ == '__main__':
    unittest.main()
