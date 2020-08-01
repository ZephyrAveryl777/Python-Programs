print("---------METHOD 1-------------")
total = 0
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements of the list: {list}")
#Iterate each element in the list
#add them in variable total
for element in range(n):
	total=total+list[element]
#printing total value
print(f"sum of elements of the list: {total}")

print("------------METHOD 2----------------")
total = 0
element = 0
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements of the list: {list}")
while element < n:
	total=total+list[element]
	element=element+1
print(f"sum of elements of the list: {total}")

print("--------------METHOD 3--------------")
#recursive way
list=[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements of the list: {list}")
def sumOfList(list,size):
	if size==0:
		return 0
	else:
		return list[size-1]+sumOfList(list, size-1)

total= sumOfList(list,n)
print(f"sum of elements of the list: {total}")

print("---------------METHOD 4-----------------")
list =[]
n=int(input("Enter size of list: "))
for i in range(n):
	data=int(input("Enter elements of the list: "))
	list.append(data)
print(f"elements of the list: {list}")
total=sum(list)
print(f"sum of elements of the list: {total}")
