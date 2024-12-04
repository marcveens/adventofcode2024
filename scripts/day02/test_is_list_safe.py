import unittest

from is_list_safe import is_list_safe


class TestIsListSafe(unittest.TestCase):
    def test_list_01(self):
        self.assertEqual(is_list_safe([7, 6, 4, 2, 1]), True)
        
    def test_list_02(self):
        self.assertEqual(is_list_safe([1, 2, 7, 8, 9]), False)
        
    def test_list_03(self):
        self.assertEqual(is_list_safe([9, 7, 6, 2, 1]), False)
        
    def test_list_04(self):
        self.assertEqual(is_list_safe([1, 3, 2, 4, 5]), False)
        
    def test_list_05(self):
        self.assertEqual(is_list_safe([8, 6, 4, 4, 1]), False)
        
    def test_list_06(self):
        self.assertEqual(is_list_safe([1, 3, 6, 7, 9]), True)
        
if __name__ == '__main__':
    unittest.main()