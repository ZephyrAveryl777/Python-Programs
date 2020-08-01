"""
Problem Description
A list is given in which all elements except one element occurs an even number of times. The problem is to find the element that occurs an odd number of times.
Problem Solution
1. The function find_odd_occurring is defined.
2. It takes a list as argument which has only one element that occurs an odd number of times.
3. The function returns that element.
4. It finds the element by XORing all elements in the list.
5. Since the XOR operation is commutative and associative and it satisfies p XOR p = 0 and p XOR 0 = p, the element that occurs an odd number of times is the result.
"""
def find_odd_occurring(alist):
	"""Return the element that occurs an odd number of times in alist.
	alist is a list in which all elements except one element occurs an even number of times."""
	ans=0
	for element in alist:
		ans^= element
	return ans
alist=input("Enter the list: ").split()
alist=[int(i) for i in alist]
ans=find_odd_occurring(alist)
print(f"The element that occurs odd number of times: {ans}")