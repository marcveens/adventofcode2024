import unittest

from path_walker import path_walker

class TestValidatePathWalker(unittest.TestCase):        
    def test_path_walker_01(self):
        self.assertEqual(path_walker("test_input_01.txt"), 41)
        
if __name__ == '__main__':
    unittest.main()