import unittest
from Josephus import josephus

class TestCaseJosephus(unittest.TestCase): 
  def test_basic_case(self):
    self.assertEqual(josephus(4, 2), 1, "josephus(4, 2) should return 1")

  def test_single_friend(self):
    self.assertEqual(josephus(1, 5), 1, "josephus(1, 5) should return 1")

  def test_k_greater_than_n(self):
    self.assertEqual(josephus(5, 10), 4, "josephus(5, 10) should return 4")

  def test_k_is_one(self):
    self.assertEqual(josephus(6, 1), 6, "josephus(6, 1) should return 6")

  def test_large_values(self):
    self.assertEqual(josephus(100, 15), 42, "josephus(100, 15) should return 37")

  def test_n_and_k_equal(self):
    self.assertEqual(josephus(3, 3), 2, "josephus(3, 3) should return 2")

  def test_n_two_k_one(self):
    self.assertEqual(josephus(2, 1), 2, "josephus(2, 1) should return 2")

  def test_n_two_k_two(self):
    self.assertEqual(josephus(2, 2), 1, "josephus(2, 2) should return 1")
    
if __name__ == '__main__':
  unittest.main()