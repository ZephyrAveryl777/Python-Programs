""" 
Problem Description
We are given a Gray codeword. We have to find the associated binary number.
Problem Solution
1. The function gray_to_binary is defined.
2. It takes the Gray codeword string as argument.
3. It returns its associated binary number as a string.
4. If g(i) is the ith bit in the Gray codeword and b(i) is the ith bit in its associated binary number 
where the 0th bit is the MSB, it can be shown g(0) = b(0) and b(i) = g(i) XOR b(i – 1) for i > 0.
5. From the above, it follows that b(i) = g(i) XOR g(i – 1) XOR … XOR g(0).
6. Thus a Gray codeword g can be converted to its associated binary number 
by performing (g XOR (g >> 1) XOR (g >> 2) XOR … XOR (g >> m)) where m is such that g >> (m + 1) equals 0.
"""
def gray_to_binary(n):
	"""Convert Gray codeword to binary and return it"""
	mask=n=int(n,2) # Convert to int
	while mask != 0:
		mask >>= 1
		n ^= mask
	return bin(n)[2:]
		# bin(n) returns n's binary representation with a '0b' prefixed
                                # the slice operation is to remove the prefix
                
g=input("Enter Grey Codeword: ")
b=gray_to_binary(g)
print(f"In binary: {b}")

