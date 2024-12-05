import unittest

from validate_manual import validate_manual

class TestValidateManual(unittest.TestCase):        
    def test_validate_manual_01(self):
        self.assertEqual(validate_manual("test_input_01.txt"), 123)
        
if __name__ == '__main__':
    unittest.main()