import unittest
from climbing import climbing

class TestClimbStairs(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(climbing(1), 1, "Should be 1 way to climb 1 step")
        self.assertEqual(climbing(2), 2, "Should be 2 ways to climb 2 steps")

    def test_small_number_of_steps(self):
        self.assertEqual(climbing(3), 3, "Should be 3 ways to climb 3 steps")
        self.assertEqual(climbing(4), 5, "Should be 5 ways to climb 4 steps")

    def test_medium_number_of_steps(self):
        self.assertEqual(climbing(5), 8, "Should be 8 ways to climb 5 steps")
        self.assertEqual(climbing(6), 13, "Should be 13 ways to climb 6 steps")

    def test_large_number_of_steps(self):
        self.assertEqual(climbing(10), 89, "Should be 89 ways to climb 10 steps")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            climbing("not a number")
            climbing(None)

if __name__ == '__main__':
    unittest.main()