import unittest
from subset import powerSet

class TestPowerSet(unittest.TestCase):
    def test_power_set_empty_array(self):
        nums = []
        result = powerSet(nums)
        expected = {()}
        self.assertEqual(set(map(tuple, result)), expected, "Expected the power set of an empty array to contain only an empty subset")

    def test_power_set_single_element_array(self):
        nums = [1]
        result = powerSet(nums)
        expected = {(), (1,)}
        self.assertEqual(set(map(tuple, result)), expected, "Expected the power set of a single-element array to contain an empty subset and the element itself")

    def test_power_set_two_elements_array(self):
        nums = [1, 2]
        result = powerSet(nums)
        expected = {(), (1,), (2,), (1, 2)}
        self.assertEqual(set(map(tuple, result)), expected, "Expected the power set of a two-elements array to contain four subsets")

    def test_power_set_three_elements_array(self):
        nums = [1, 2, 3]
        result = powerSet(nums)
        expected = {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}
        self.assertEqual(set(map(tuple, result)), expected, "Expected the power set of a three-elements array to contain eight subsets")

    # Add more test cases as needed for different input arrays

if __name__ == '__main__':
    unittest.main()