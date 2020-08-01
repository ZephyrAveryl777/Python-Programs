##This is a Python Program to print all integers that aren’t divisible by either 2 or 3 and lies between 1 and 50.
lower =int(input("Enter the lower limit of the range: "))
upper = int(input("Enter the upper limit of the range: "))
l=[]
for i in range(lower,upper):
    if i%2==0 and i%3 == 0:
        l.append(i)
print("The integers which are divisible by either 2 or 3 are:\n",l)
