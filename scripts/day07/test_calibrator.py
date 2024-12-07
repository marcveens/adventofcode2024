import unittest

from calibrator import calibrate

class TestCalibrator(unittest.TestCase):        
    def test_calibrate_01(self):
        self.assertEqual(calibrate("test_input_01.txt"), 3749)
        
if __name__ == '__main__':
    unittest.main()