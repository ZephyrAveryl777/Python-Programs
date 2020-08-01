"""
Problem Description
A number is given. We have to clear the rightmost set bit of the number. 
That is, we have to flip the rightmost 1 in the binary representation of n.
Problem Solution
1. The function clear_rightmost_set_bit is defined.
2. It takes a number n as argument and returns n with its rightmost set bit cleared.
3. This is done by computing n & (n – 1) and returning it.
4. (n – 1) equals n with all the rightmost consecutive 0s and the first rightmost 1 flipped.
5. Thus n & (n – 1) equals n with its rightmost 1 cleared.
"""
def clear_rightmost_set_bit(n):
	"""Clear rightmost set bit of n and return it."""
	return n & (n-1)
n=int(input("Enter a number: "))
ans= clear_rightmost_set_bit(n)
print(f"{n} in binary = {bin(n)}, with its rightmost bit cleared equals: {ans}, which in binary format equals to ({bin(ans)})")