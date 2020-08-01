"""
Problem Description
The program finds a subarray that has the maximum sum within the given array.
Problem Solution
1. Define the function find_max_subarray that takes a list as argument and two indexes, start and end. 
It finds the maximum subarray in the range [start, end – 1].
2. The function find_max_subarray returns the tuple (l, r, m) where l, r are the left and right indexes 
of the maximum subarray and m is its sum.
3. The base case is when the input list is just one element (i.e. start == end – 1).
4. Otherwise, the list is divided into two and find_max_subarray is called on both the halves.
5. The maximum subarray is either the maximum subarray of one of the halves or the maximum subarray 
crossing the midpoint of the two halves.
6. The function find_max_crossing_subarray takes a list as argument and three indexes, start, mid and end 
and finds the maximum subarray containing mid.
"""
def find_max_subarray(alist, start, end):
    """Returns (l, r, m) such that alist[l:r] is the maximum subarray in
    A[start:end] with sum m. Here A[start:end] means all A[x] for start <= x <
    end."""
    # base case
    if start == end - 1:
        return start, end, alist[start]
    else:
        mid = (start + end)//2
        left_start, left_end, left_max = find_max_subarray(alist, start, mid)
        right_start, right_end, right_max = find_max_subarray(alist, mid, end)
        cross_start, cross_end, cross_max = find_max_crossing_subarray(alist, start, mid, end)
        if (left_max > right_max and left_max > cross_max):
            return left_start, left_end, left_max
        elif (right_max > left_max and right_max > cross_max):
            return right_start, right_end, right_max
        else:
            return cross_start, cross_end, cross_max
 
def find_max_crossing_subarray(alist, start, mid, end):
    """Returns (l, r, m) such that alist[l:r] is the maximum subarray within
    alist with start <= l < mid <= r < end with sum m. The arguments start, mid,
    end must satisfy start <= mid <= end."""
    sum_left = float('-inf')
    sum_temp = 0
    cross_start = mid
    for i in range(mid - 1, start - 1, -1):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_left:
            sum_left = sum_temp
            cross_start = i
 
    sum_right = float('-inf')
    sum_temp = 0
    cross_end = mid + 1
    for i in range(mid, end):
        sum_temp = sum_temp + alist[i]
        if sum_temp > sum_right:
            sum_right = sum_temp
            cross_end = i + 1
    return cross_start, cross_end, sum_left + sum_right
 
alist = input('Enter the list of numbers: ')
alist = alist.split()
alist = [int(x) for x in alist]
start, end, maximum = find_max_subarray(alist, 0, len(alist))
print('The maximum subarray starts at index {}, ends at index {}'
      ' and has sum {}.'.format(start, end - 1, maximum))