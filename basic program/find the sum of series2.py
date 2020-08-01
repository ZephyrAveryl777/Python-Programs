#This is a Python Program to find the sum of series: 1 + x^2/2 + x^3/3 + … x^n/n.
"""Problem Solution
1. Take in the number of terms to find the sum of the series for.
2. Initialize the sum variable to 0.
3. Use a for loop ranging from 1 to the number and find the sum of the series.
4. Print the sum of the series after rounding it off to two decimal places.
5. Exit.
"""
n=int(input("Enter the number of terms in the series: "))
x=int(input("Enter the value of x: "))
sum=1
print("The sum of series is: 1+",end=" ")
for i in range(2,n+1):
	print(f"{i}^{i}/{i}",sep=" ",end=" ")
	if i<n:
		print("+",sep=" ",end=" ")
	sum=sum+((x**i)/1)
print(f" = {round(sum,3)}")
print()