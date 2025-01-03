import sys
import io, unittest
from unittest import TestCase
from Tower_Hanoi import TowerHanoi 

class Evaluate(TestCase):

    def assertTohOutput(self, n, expected_output):
        original_stdout = sys.stdout  # Save the original stdout
        sys.stdout = buffer = io.StringIO()  # Redirect stdout to a string buffer
        actual_moves = TowerHanoi(n, 'A', 'C', 'B')  # Call the toh function
        sys.stdout = original_stdout  # Reset stdout
        actual_output = buffer.getvalue().strip()
        self.assertEqual(actual_output, expected_output.strip(), 
                         f"Printed output for {n} disks is incorrect.\nExpected:\n{expected_output}\nActual:\n{actual_output}")
        self.assertEqual(actual_moves, 2**n - 1, 
              f"Incorrect number of moves for {n} disks. Expected: {2**n - 1}, Actual: {actual_moves}")

    def test_toh_1_disk(self):
        expected_output = "move disk 1 from rod A to rod C"
        self.assertTohOutput(1, expected_output)

    def test_toh_2_disks(self):
        expected_output = (
            "move disk 1 from rod A to rod B\n"
            "move disk 2 from rod A to rod C\n"
            "move disk 1 from rod B to rod C"
        )
        self.assertTohOutput(2, expected_output)

    def test_toh_3_disks(self):
        expected_output = (
            "move disk 1 from rod A to rod C\n"
            "move disk 2 from rod A to rod B\n"
            "move disk 1 from rod C to rod B\n"
            "move disk 3 from rod A to rod C\n"
            "move disk 1 from rod B to rod A\n"
            "move disk 2 from rod B to rod C\n"
            "move disk 1 from rod A to rod C"
        )
        self.assertTohOutput(3, expected_output)

    def test_toh_4_disks(self):
        expected_output = (
            "move disk 1 from rod A to rod B\n"
            "move disk 2 from rod A to rod C\n"
            "move disk 1 from rod B to rod C\n"
            "move disk 3 from rod A to rod B\n"
            "move disk 1 from rod C to rod A\n"
            "move disk 2 from rod C to rod B\n"
            "move disk 1 from rod A to rod B\n"
            "move disk 4 from rod A to rod C\n"
            "move disk 1 from rod B to rod C\n"
            "move disk 2 from rod B to rod A\n"
            "move disk 1 from rod C to rod A\n"
            "move disk 3 from rod B to rod C\n"
            "move disk 1 from rod A to rod B\n"
            "move disk 2 from rod A to rod C\n"
            "move disk 1 from rod B to rod C"
        )
        self.assertTohOutput(4, expected_output)
if __name__ == '__main__':
  unittest.main()