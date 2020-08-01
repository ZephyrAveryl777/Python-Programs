#Python Program to form an integer that has the number of digits at the ten’s place and the least significant digit in the one’s place.
temp=n=int(input("Enter the number: "))
k=0
while n>0:
	print(f"k value {k} now k after incrementing becomes k = {k+1}")
	k=k+1
	print(f"number initally n= 129, after n//10 = {n} // {10}, hecne value of n = {n//10}")
	n=n//10
b=str(temp)
print(f"temp = {temp} and b = {b}")
c=str(k)
print(f"c = {c} and k = {k}")
d=c+b[k-1]
print(f"the value of b[k-1] = {b[k-1]}")
print(f"The new number formed is: {int(d)}")