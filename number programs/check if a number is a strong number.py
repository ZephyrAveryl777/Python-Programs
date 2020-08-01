""""Strong number is a special number whose sum of factorial of digits is equal to the original number.
For example: 145 is strong number. Since, 1! + 4! + 5! = 145"""
sum=0
temp=number = int(input("Enter a number: "))
while number:
	i=f=1
	r=number%10
	while i<=r:
		f=f*i
		i=i+1
	sum=sum+f
	number=number//10
if sum==temp:
	print(f"The number {temp} is a strong number!")
else:
    print(f"The number {temp} is not a Strong number!")	