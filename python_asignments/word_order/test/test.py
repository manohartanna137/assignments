import unittest
from word_order.core.utils import *



class testcase(unittest.TestCase):
    def test_word(self):
        n=4
        i = ['bcd','abc','bcd','bcd']
        actualinput = word_order(n,i)
        expectedoutput = [2, 1, 1]
        self.assertEqual(actualinput, expectedinput)

if __name__ == '__main__':
    unittest.main()
