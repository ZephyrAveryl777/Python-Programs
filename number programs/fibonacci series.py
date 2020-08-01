"""Fibonacci sequence:
The Fibonacci sequence specifies a series of numbers where the next number is found by 
adding up the two numbers just before it.
Example: 0,1,1,2,3,5,8,13,21,34,.....
""" 
n=int(input("How many terms do you want? : "))
#first two terms
n1=0
n2=1
count=2
#Check if number is valid 
if n<=0:
	print("Please enter a positive integer! ")
elif n==1:
	print("Fibonacci sequence:")
	print(n1)
else:
	print("Fibonacci sequence:")
	print(n1,",",n2,end=",")
	while count<n:
		nth = n1+n2
		print(nth,end=',')
		#update values
		n1=n2
		n2=nth
		count += 1

