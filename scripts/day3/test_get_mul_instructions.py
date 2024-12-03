import unittest

from get_mul_instructions import get_mul_instructions


class TestGetMulInstructions(unittest.TestCase):
    # def test_mul_01(self):
    #     self.assertEqual(get_mul_instructions("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"), [
    #         {
    #             "raw": "mul(2,4)",
    #             "values": [2, 4],
    #             "outcome": 8
    #         },
    #         {
    #             "raw": "mul(5,5)",
    #             "values": [5, 5],
    #             "outcome": 25
    #         },
    #         {
    #             "raw": "mul(11,8)",
    #             "values": [11, 8],
    #             "outcome": 88
    #         },
    #         {
    #             "raw": "mul(8,5)",
    #             "values": [8, 5],
    #             "outcome": 40
    #         },
    #     ])
    
    # def test_mul_01_result(self):
    #     results = get_mul_instructions("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    #     outcome = 0
        
    #     for item in results:
    #         outcome += item.get("outcome")
            
    #     self.assertEqual(outcome, 161)
        
    def test_mul_02(self):
        self.assertEqual(get_mul_instructions("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"), [
            {
                "raw": "mul(2,4)",
                "values": [2, 4],
                "outcome": 8
            },
            {
                "raw": "mul(8,5)",
                "values": [8, 5],
                "outcome": 40
            },
        ])
    
    def test_mul_02_result(self):
        results = get_mul_instructions("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
        outcome = 0
        
        for item in results:
            outcome += item.get("outcome")
            
        self.assertEqual(outcome, 48)
        
if __name__ == '__main__':
    unittest.main()