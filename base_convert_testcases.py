import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):
    """ This test to see if the function accurately
    converts the number into the correct base assigned.
    Also if base >= 10, convert it to the corresponding variable.
    """
    
    # Testing if the function works
    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
    
    def test_base(self):
        self.assertEqual(convert(11259375,16), 'ABCDEF')

        self.assertEqual(convert(312344, 13), 'AC226')

        self.assertEqual(convert(18724, 16), '4924')

        self.assertEqual(convert(18724, 15), '5834')

        self.assertEqual(convert(93789, 14), '26273')


if __name__ == "__main__":
        unittest.main()