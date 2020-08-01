#Amicable numbers - a pair of numbers, each of which is the sum of the factors of the other (e.g. 220 and 284).
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
sum1=0
sum2=0
for i in range(1,x):
	if x%i == 0:
		sum1+=i
for j in range(1,y):
	if y%j == 0:
		sum2+=j
if sum1==y and sum2==y:
	print(f"The numbers {x} and {y} are Amicable!")
else:
	print(f"The numbers {x} and {y} are not Amicable!")
