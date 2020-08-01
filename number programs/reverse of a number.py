print("--+++++++++++++++++++Method 1--+++++++++++++++++++++++")
temp = num=int(input("Enter the number as per your choice: "))
rev=0
while num>0:
    rev=(rev*10)+(num%10)
    num=num//10
print("Reverse of the number {0} is: {1}".format(temp,rev))
print("--+++++++++++++++++++Method 2--+++++++++++++++++++++++")
temp = num=int(input("Enter the number as per your choice: "))
rev=0
def Reverse(num):
    global rev
    if num>0 :
        rev=(rev*10)+(num%10)
        Reverse(num//10)
    return rev
rev=Reverse(num)
print("Reverse of the number {0} is: {1}".format(temp,rev))
print("-------------------------------------------------")
