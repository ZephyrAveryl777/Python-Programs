"""
Problem Description
The program finds a subarray that has the maximum sum within the given array.
Problem Solution
1. Define the function find_max_subarray that takes a list as argument and two indexes, start and end. 
It finds the maximum subarray in the range [start, end – 1].
2. The function find_max_subarray returns the tuple (l, r, m) where l, r are
the left and right indexes of the maximum subarray and m is its sum.
3. The function uses a loop to keep track of the maximum subarray ending at index i. 
That is, the maximum subarray that has the element at index i as its last element.
4. Then the maximum subarray will simply be the maximum of all these subarrays.
5. The maximum subarray ending at index i + 1 is given by
max(list[i] + maximum sum of subarray ending at i, list[i]).
6. The function keeps track of the maximum sum of the subarray 
seen so far and its left, right indexes as the loop iterates.
"""
def find_max_subarray(alist, start, end):
    """Returns (l, r, m) such that alist[l:r] is the maximum subarray in
    A[start:end] with sum m. Here A[start:end] means all A[x] for start <= x <
    end."""
    max_ending_at_i = max_seen_so_far = alist[start]
    max_left_at_i = max_left_so_far = start
    # max_right_at_i is always i + 1
    max_right_so_far = start + 1
    for i in range(start + 1, end):
        if max_ending_at_i > 0:
            max_ending_at_i += alist[i]
        else:
            max_ending_at_i = alist[i]
            max_left_at_i = i
        if max_ending_at_i > max_seen_so_far:
            max_seen_so_far = max_ending_at_i
            max_left_so_far = max_left_at_i
            max_right_so_far = i + 1
    return max_left_so_far, max_right_so_far, max_seen_so_far
 
 
alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
start, end, maximum = find_max_subarray(alist, 0, len(alist))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end - 1, maximum))
