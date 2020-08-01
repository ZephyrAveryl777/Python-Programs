"""
The program finds the number of ones in the binary representation of a number.
Problem Solution
1. Create a function count_set_bits that takes a number n as argument.
2. The function works by performing bitwise AND of n with n – 1 and storing the result in n until n becomes 0.
3. Performing bitwise AND with n – 1 has the effect of clearing the rightmost set bit of n.
4. Thus the number of operations required to make n zero is the number of set bits in n.
"""
def count_set_bits(n):
	count = 0
	while n:
		n &= n-1
		count += 1
	return count
n=int(input("Enter a number: "))
print(f"Number of set bits (number of ones) in number = {n} where binary of the number  = {bin(n)} is {count_set_bits(n)}")