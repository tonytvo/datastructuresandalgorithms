import pytest
from src.mergesort import sort

class TestMergeSort:
    def test_sort_6_should_be_move_to_the_third_last_element(self):
        sequence = [6, 5, 3, 1, 8, 7, 2, 4]
        merged_sort_sequence = sort(sequence)
        assert merged_sort_sequence == [1, 2, 3, 4, 5, 6, 7, 8]
