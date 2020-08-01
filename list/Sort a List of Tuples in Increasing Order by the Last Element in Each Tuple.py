"""
Problem Description
The program takes a list of tuples and sorts the list of tuples in increasing order by the last element in each tuple.

Problem Solution
1. Take a list of tuples from the user.
2. Define a function which returns the last element of each tuple in the list of tuples.
3. Define another function with the previous function as the key and sort the list.
4. Print the sorted list.
5. Exit.
"""
def last(n):
	return n[-1]

def sort(tuples):
	return sorted(tuples,key=last)

a=input("Enter a list of tuples: ")
print(f"Sorted: {sort(a)}")