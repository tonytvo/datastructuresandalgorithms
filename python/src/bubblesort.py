# T: time complexity
# S: space complexity
# T: O(n^2)
# S: O(1)
from unittest.util import sorted_list_difference


def sort(seq):
    n = len(seq)
    i = 0
    j = 1
    end = n - 1
    while i < end:
        bubble_largest_element(end, i, j, seq)

        # at point in execution, the max in the array already in the last position
        # so we don't have to check this position anymore
        # we move end pointer to the left, in order to not check this position anymore
        end -= 1
        # move i and j back to starting position
        i = 0
        j = 1

def bubble_largest_element(end, i, j, seq):
    while j <= end:
        # swap check
        if seq[i] > seq[j]:
            temp = seq[i]
            seq[i] = seq[j]
            seq[j] = temp

        # move i and j to the next 2 element
        j += 1
        i += 1


sorted_sequence = [6, 5, 3, 1, 8, 7, 2, 4]
sort(sorted_sequence)
print(sorted_sequence)

sequence_snapshot = [6, 5, 3, 1, 8, 7, 2, 4]
bubble_largest_element(7, 0, 1, sequence_snapshot)
print(sequence_snapshot)