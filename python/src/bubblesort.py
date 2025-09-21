# T: time complexity
# S: space complexity
# T: O(n^2)
# S: O(1)
from unittest.util import sorted_list_difference


def sort(seq):
    seq_length = len(seq)
    i = 0
    j = 1
    end = seq_length - 1
    while i < end:
        bubble_largest_element(end, i, j, seq)

        # at point in execution, the max in the array already in the last position
        # so we don't have to check this position anymore
        # we move end pointer to the left, in order to not check this position anymore
        end -= 1
        # move i and j back to starting position
        i = 0
        j = 1

def bubble_largest_element(current_iteration_last_index, current_element_pointer, next_element_pointer, seq):
    while next_element_pointer <= current_iteration_last_index:
        # swap check
        if seq[current_element_pointer] > seq[next_element_pointer]:
            temp = seq[current_element_pointer]
            seq[current_element_pointer] = seq[next_element_pointer]
            seq[next_element_pointer] = temp

        # move i and j to the next 2 element
        next_element_pointer += 1
        current_element_pointer += 1

