import unittest

from subSet1 import powerSetDup

class TestSubsetsWithDup(unittest.TestCase):

    def test_unique_elements(self):
        self.assertCountEqual(powerSetDup([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
                              "Failed to handle array with unique elements.")

    def test_with_duplicates(self):
        self.assertCountEqual(powerSetDup([1, 2, 2]), [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]],
                              "Failed to handle array with duplicates correctly.")

    def test_empty_array(self):
        self.assertCountEqual(powerSetDup([]), [[]], "Failed to handle empty array.")

    def test_single_element(self):
        self.assertCountEqual(powerSetDup([1]), [[], [1]], "Failed to handle single element array.")

    def test_large_array(self):
        result = powerSetDup([1, 2, 3, 4])
        self.assertEqual(len(result), 16, "Failed to handle large array correctly. Expected 16 subsets.")  # 2^4 subsets

    def test_negative_numbers_and_duplicates(self):
        self.assertCountEqual(powerSetDup([-1, -1, 2]), [[], [-1], [-1, -1], [2], [-1, 2], [-1, -1, 2]],
                              "Failed to handle array with negative numbers and duplicates.")

if __name__ == '__main__':
    unittest.main()