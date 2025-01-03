import unittest
from Power_Sum import powerSum
class TestCasePow(unittest.TestCase):
  def single_num(self):
    self.assertEqual(powerSum([5]), 5, "Expected output is 5")
    def multiple_1_dim(self):
      self.assertEqual(powerSum([1,2,3]), 1+2+3, "Expected output is 6")
    def power_sum_nested(self):
      self.assertEqual(powerSum([2,3,[4,1,2]]), 2+3+(4+1+2)**2)
    def power_sum_deeply_nested(self):
      self.assertEqual(powerSum([1,2,[7,[3,4],2]]), 1+2+(7+(3+4)**3 + 2)**2)
if __name__ == "__main__": 
  unittest.main()