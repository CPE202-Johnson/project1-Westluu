import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    """ Test if the Bears function checks if it's possible to get 42
        with set conditions"""
    
    def test_bears(self):
        
        # Testing if not possible to get 42
        self.assertFalse(bears(100))

        self.assertFalse(bears(53))

        self.assertFalse(bears(41))

        self.assertFalse(bears(177))

        
        # Testing if possible to get 42
        self.assertTrue(bears(250))

        self.assertTrue(bears(42))

        self.assertTrue(bears(84))

        self.assertTrue(bears(168))

    

if __name__ == "__main__":
    unittest.main()
