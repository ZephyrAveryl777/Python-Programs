"""
Problem Description
The program takes in the number of elements and generates random numbers from 1 to 20 and appends them to the list.

Problem Solution
1. Import the random module into the program.
2. Take the number of elements from the user.
3. Use a for loop, random.randint() is used to generate random numbers which are them appending to a list.
4. Then print the randomised list.
4. Exit.
"""
import random
a=[]
n=int(input("Enter number of elements: "))
for i in range(n):
	a.append(random.randint(1,20))
print(f"randomised list: {a}")