import unittest
from combinatorics_sum3 import comb3

class TestCombinationSum3(unittest.TestCase):
    def test_small_combination(self):
        k = 3
        n = 7
        expected = [[1, 2, 4]]
        result = comb3(k, n)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for k={k}, n={n}")

    def test_large_combination(self):
        k = 3
        n = 9
        expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        result = comb3(k, n)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for k={k}, n={n}")

    def test_no_combination(self):
        k = 4
        n = 1
        expected = []
        result = comb3(k, n)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for k={k}, n={n}, expected no combinations")

    def test_single_combination(self):
        k = 1
        n = 9
        expected = [[9]]
        result = comb3(k, n)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for k={k}, n={n}")

    def test_all_numbers_combination(self):
        k = 9
        n = 45  # Sum of 1 through 9
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        result = comb3(k, n)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for k={k}, n={n}")

    def test_no_valid_combination(self):
        k = 3
        n = 2  # Not possible to have 3 numbers from 1 to 9 sum up to 2
        expected = []
        result = comb3(k, n)
        self.assertEqual(sorted(result), sorted(expected), "Failed when no valid combination exists")

    def test_edge_case_high_n(self):
        k = 3
        n = 24  # Only one combination of the three highest numbers
        expected = [[7, 8, 9]]
        result = comb3(k, n)
        self.assertEqual(sorted(result), sorted(expected), f"Failed for k={k}, n={n}, a high sum with limited combinations")

if __name__ == '__main__':
    unittest.main()