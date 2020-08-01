a=int(input("Enter a number: "))
k=0
for i in range(2,a//2+1):
	if a%i==0:
		k=k+1
if k<=0:
	print(f"The number {a} is prime!")
else:
	print(f"The number {a} is not prime!")