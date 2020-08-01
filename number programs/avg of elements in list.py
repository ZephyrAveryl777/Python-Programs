###Problem Description
##The program takes the elements of the list one by one and displays the average of the elements of the list.
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("\nEnter element at position "+str(i)+": "))
    a.append(elem)
    print("Elements in the list after appendinga are: ", a)
avg=sum(a)/n
print("\nAverage of element in the list",a,"is :",  round(avg,2))
