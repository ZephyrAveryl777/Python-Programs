print("----------------Method 1-----------------------")
temp=n=int(input("Enter the number: "))
count = 0
while n>0:
    count =count+1
    n=n//10
print("The number of digits in the number {0} are: {1} ".format(temp,count))
print("----------------Method 2-----------------------")
temp=Number=int(input("Enter the number: "))

def Counting(Number):
    Count = 0
    while(Number > 0):
        Number = Number // 10
        Count = Count + 1
    return Count

print("The number of digits in the number {0} are: {1} ".format(temp,Counting(Number))) 
