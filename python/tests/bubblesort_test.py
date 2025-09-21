import pytest
from src.bubblesort import sort
import src.bubblesort as bubblesort

class TestBubbleSort:
    def test_sort_6_should_be_move_to_the_third_last_element(self):
        sorted_sequence = [6, 5, 3, 1, 8, 7, 2, 4]
        sort(sorted_sequence)
        assert sorted_sequence == [1, 2, 3, 4, 5, 6, 7, 8]

    def test_sort_should_bubble_largest_element_8_to_last_index(self):
        sequence_snapshot = [6, 5, 3, 1, 8, 7, 2, 4]
        bubblesort.bubble_largest_element(7, 0, 1, sequence_snapshot)
        assert sequence_snapshot == [5, 3, 1, 6, 7, 2, 4, 8]
