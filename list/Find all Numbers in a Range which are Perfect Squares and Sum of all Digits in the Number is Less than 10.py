"""
Problem Description
The program takes a range and creates a list of all numbers in the range which are perfect squares and the sum of the digits is less than 10.
Problem Solution
1. User must enter the upper and lower range for the numbers.
2. A list must be created using list comprehension where the element is a perfect square within the range and the sum of the digits of the number is less than 10.
3. This list must then be printed.
4. Exit.
"""
l=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
a=[]
a=[x for x in range(1,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)