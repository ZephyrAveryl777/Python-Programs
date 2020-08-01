#Python Program to check if a number is an Armstrong number..
n = int(input("Enter the number: "))
a = list(map(int,str(n)))
print(f"the value of a in the program {a}")
b = list(map(lambda x:x**3,a))
print(f"the value of b in the program {b} and sum of elements in b is: {sum(b)}")
if sum(b)==n:
	print(f"The number {n} is an armstrong number.")
else:
	print(f"The number {n} is not an armstrong number.")