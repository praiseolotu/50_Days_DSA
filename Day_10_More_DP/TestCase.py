import unittest
from min_climb import min_climb

class TestMinCostClimbingStairs(unittest.TestCase):
    def test_single_step(self):
        self.assertEqual(min_climb([10]), 0, "Minimum cost for single step should be 0")

    def test_two_steps(self):
        self.assertEqual(min_climb([10, 15]), 10, "Minimum cost for two steps should be the cost of the cheaper step")

    def test_example_case(self):
        self.assertEqual(min_climb([10, 15, 20]), 15, "Minimum cost for example case should be 15")

    def test_longer_sequence(self):
        self.assertEqual(min_climb([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6, "Minimum cost for a longer sequence should be calculated correctly")

    def test_start_from_second_step(self):
        self.assertEqual(min_climb([0, 0, 0, 1]), 0, "It should be possible to start from the second step for a lower cost")

    def test_zero_cost_steps(self):
        self.assertEqual(min_climb([0, 0, 0, 0]), 0, "Minimum cost with all zero cost steps should be 0")

if __name__ == '__main__':
    unittest.main()
