import unittest
from list_methods.core.driver import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        x = ['insert 0 5', 'insert 1 10', 'append 15', 'sort', 'remove 10', 'reverse', 'pop', 'print']
        actualinput= list_methods(x)
        expectedoutput=[15]
        self.assertEqual(actualinput,expectedoutput)
if __name__ == '__main__':
    unittest.main()
