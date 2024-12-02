import unittest

from is_list_almost_safe import is_list_almost_safe


class TestIsListAlmostSafe(unittest.TestCase):
    def test_list_01(self):
        self.assertEqual(is_list_almost_safe([7, 6, 4, 2, 1]), True)
        
    def test_list_02(self):
        self.assertEqual(is_list_almost_safe([1, 2, 7, 8, 9]), False)
        
    def test_list_03(self):
        self.assertEqual(is_list_almost_safe([9, 7, 6, 2, 1]), False)
        
    def test_list_04(self):
        self.assertEqual(is_list_almost_safe([1, 3, 2, 4, 5]), True)
        
    def test_list_05(self):
        self.assertEqual(is_list_almost_safe([8, 6, 4, 4, 1]), True)
        
    def test_list_06(self):
        self.assertEqual(is_list_almost_safe([1, 3, 6, 7, 9]), True)
    
    def test_list_07(self):    
        self.assertEqual(is_list_almost_safe([48, 46, 47, 49, 51, 54, 56]), True)
    
    def test_list_08(self):
        self.assertEqual(is_list_almost_safe([1, 1, 2, 3, 4, 5]), True)
    
    def test_list_09(self):
        self.assertEqual(is_list_almost_safe([1, 2, 3, 4, 5, 5]), True)
    
    def test_list_10(self):
        self.assertEqual(is_list_almost_safe([5, 1, 2, 3, 4, 5]), True)
    
    def test_list_11(self):
        self.assertEqual(is_list_almost_safe([1, 4, 3, 2, 1]), True)
    
    def test_list_12(self):
        self.assertEqual(is_list_almost_safe([1, 6, 7, 8, 9]), True)
    
    def test_list_13(self):
        self.assertEqual(is_list_almost_safe([1, 2, 3, 4, 3]), True)
    
    def test_list_14(self):
        self.assertEqual(is_list_almost_safe([9, 8, 7, 6, 7]), True)
    
    def test_list_16(self):
        self.assertEqual(is_list_almost_safe([7, 10, 8, 10, 11]), True)
    
    def test_list_17(self):
        self.assertEqual(is_list_almost_safe([29, 28, 27, 25, 26, 25, 22, 20]), True)
        
if __name__ == '__main__':
    unittest.main()