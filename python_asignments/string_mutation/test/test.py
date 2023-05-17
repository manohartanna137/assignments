import unittest
from string_mutation.core.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actualoutput= mutate_string("DIGGIYTE",5,"B")
        expectedoutput="DIGGIBYTE"

        self.assertEqual(actualoutput,expectedoutput)  # add assertion here
    def test_somethin(self):
        actualoutput= mutate_string("Maohar",2,"n")
        expectedoutput="Manohar"

        self.assertEqual(actualoutput,expectedoutput)  # add assertion here

if __name__ == '__main__':
    unittest.main()
