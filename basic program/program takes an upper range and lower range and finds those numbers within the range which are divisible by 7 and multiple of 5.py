#program takes an upper range and lower range and finds those numbers within the range which are divisible by 7 and multiple of 5
lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
for i in range(lower,upper+1):
	if i%7 == 0 and i%5==0:
		print(i)
