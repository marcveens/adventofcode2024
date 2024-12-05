import unittest

from get_xmas import get_xmas

class TestGetXmas(unittest.TestCase):        
    def test_xmas_01(self):
        self.assertEqual(get_xmas("test_input_02.txt"), 9)
        
if __name__ == '__main__':
    unittest.main()