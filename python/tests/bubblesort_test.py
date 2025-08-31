import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import bubblesort as bublesort

class MyTestCase(unittest.TestCase):
    def test_something(self):
        sorted_sequence = [6, 5, 3, 1, 8, 7, 2, 4]
        bublesort.sort(sorted_sequence)
        self.assertEqual(sorted_sequence, [1, 2, 3, 4, 6, 5, 6, 8], sorted_sequence)

        sequence_snapshot = [6, 5, 3, 1, 8, 7, 2, 4]
        bublesort.bubble_largest_element(7, 0, 1, sequence_snapshot)
        self.assertEqual([6, 5, 3, 1, 7, 2, 4, 8], sequence_snapshot)
        self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
