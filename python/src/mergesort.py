# can you do iterative merge sort?
# can you do merge sort without allocating extra space? (sort the array in place)
# Time complexity: O(nlog(n))
# Space complexity: O(n)

def sort(sequence):
    n = len(sequence)

    if n == 1:
        return sequence

    mid = n//2
    left = sort(sequence[0:mid])
    right = sort(sequence[mid:n])

    return sort_merge_left_and_right(left, right)


def sort_merge_left_and_right(left, right):
    temp = []
    left_index = 0
    right_index = 0

    # iterate left on left_index and right on right_index, compare the 2 element and place the smallest index in the temp
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            temp.append(left[left_index])
            left_index += 1
        else:
            temp.append(right[right_index])
            right_index += 1

    # at this point, we will be left with incomplete left array or incomplete right array
    while left_index < len(left):
        temp.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        temp.append(right[right_index])
        right_index += 1

    return temp

