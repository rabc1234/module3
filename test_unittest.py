import unittest
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        #Will test  the sum function

        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6, "1st test should be 6")
    
    def test_list_tuple(self):
        data2 = (1,2,4)
        result2 = sum(data2)
        self.assertEqual(result2, 6, "2nd test should be 6")
    
if __name__ == '__main__':
    unittest.main()
