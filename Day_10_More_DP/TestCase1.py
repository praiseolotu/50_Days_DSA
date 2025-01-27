import unittest

from tribonnaci import trib 

class TestTribonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(trib(0), 0, "Failed for n=0")
        self.assertEqual(trib(1), 1, "Failed for n=1")
        self.assertEqual(trib(2), 1, "Failed for n=2")

    def test_small_numbers(self):
        self.assertEqual(trib(3), 2, "Failed for n=3")
        self.assertEqual(trib(4), 4, "Failed for n=4")

    def test_larger_numbers(self):
        self.assertEqual(trib(5), 7, "Failed for n=5")
        self.assertEqual(trib(10), 149, "Failed for n=10")

    def test_high_numbers(self):
        self.assertEqual(trib(20), 66012, "Failed for n=20")
        self.assertEqual(trib(25), 1389537, "Failed for n=25")

if __name__ == '__main__':
    unittest.main()
