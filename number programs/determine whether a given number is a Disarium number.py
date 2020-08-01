"""Disarium number

A number is said to be the Disarium number 
when the sum of its digit raised to the power of their respective positions is equal to the number itself.
For example, 175 is a Disarium number as follows
1**1 + 7**2 + 5**3 = 1 + 49 + 125 = 175
Some of the other examples of Disarium number are 89, 135, 518 etc.

To find whether given number is Disarium or not, 
calculate the sum of digits powered with their respective positions. 
If the sum is equal to the original number then,
 the given number is Disarium number.
"""
n=num=int(input("Enter a number: "))#makes copy of the original numer
#length(n) will count the digits present in a number
def length(n):
	length = 0
	while n!= 0:
		length = length+1
		n=n//10
	print(f"lenth of the number {num} is {length}")
	return length
rem=sum=0
len=length(n)
#Calculate the sum of digits powered with their respective positions
print("Internal calculations: ")
while num>0:
	rem=num%10
	sum=sum+int(rem**len)
	num =num//10
	len =len-1
	print(f"{rem}**{len+1} + ={sum}")
	
#checks whether the sum is equal to the number itself
if(sum == n):
    print(f"{str(n)} is a disarium number")  
else:  
    print(f"{str(n)} is not a disarium number")  
