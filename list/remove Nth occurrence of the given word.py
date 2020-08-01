"""
Given a list of words in Python, the task is to remove the Nth occurrence of the given word in that list.
"""
print("----------METHOD 1---------------")
"""
By taking another list.
Make a new list, say newList.
Iterate the elements in the list and check if the word 
to be removed matches the element 
and the occurrence number, otherwise, append the element to newList.
"""
#Fucntion to remove Ith Word
def removeWord(list,word,N):
	newList=[]
	count=0

	#iterate the elements
	for i in list:
		if i==word:
			count=count+1
			if count!=N:
				newList.append(i)
		else:
			newList.append(i)
	list=newList
	if count==0:
		print("Item not found!")
	else:
		print(f"After removing the element at {N} the list is: ",end=" " )
	return newList

list=[]
n=int(input("Enter the size of list: "))
for i in range(n):
	data=input(f"Enter elements of the array at position {i}: ")
	list.append(data)
print("Elements in the list: ",end=" ")
for i in range(n):
	print(list[i],end=" ")
print()
word=input("Enter the word whose occurence is to be found: ")
N=int(input("Enter the occurence position to be removed: "))
print(removeWord(list,word,N))

print("---------METHOD 2------------")
"""
Remove from the list itself.
Instead of making a new list, delete the matching element from the list itself. 
Iterate the elements in the list and
check if the word to be removed matches the element and the occurrence number, 
If yes delete that item and return true.
If True is returned, print List otherwise, print “Item not Found”.
"""
def removeWord(list,word,N):
	count=0
	for i in range(0,n):
		if list[i]==word:
			count=count+1

			if count==N:
				del(list[i])
				return True
	
	return False

list=[]
n=int(input("Enter the size of list: "))
for i in range(n):
	data=input(f"Enter elements of the array at position {i}: ")
	list.append(data)
print("Elements in the list: ",end=" ")
for i in range(n):
	print(list[i],end=" ")
print()
word=input("Enter the word whose occurence is to be found: ")
N=int(input("Enter the occurence position to be removed: ")) 
flag=removeWord(list,word,N)
if flag==True:
	print(f"After removing the element at {N} the elements in the list is: {removeWord(list,word,N)} ",end=" ")
else:
	print("Item not Updated")

print("-------------METHOD 3-------------")
"""
Remove from the list using pop().

Instead of creating a new list and using if/else statement we can pop the matching element from the list using pop( ). We need to use an additional counter to keep track of the index.
because pop( ) needs index to pass inside i.e pop(index)
"""
def removeWord(list,word,N):
	count=0
	index=0
	for i in list:
		index=index+1
		if i==word:
			count=count+1
			if count==N:
				list.pop(index-1)
	return list

list=[]
n=int(input("Enter the size of list: "))
for i in range(n):
	data=input(f"Enter elements of the array at position {i}: ")
	list.append(data)
print("Elements in the list: ",end=" ")
for i in range(n):
	print(list[i],end=" ")
print()
word=input("Enter the word whose occurence is to be found: ")
N=int(input("Enter the occurence position to be removed: ")) 
print(f"New list is: {removeWord(list,word,N)}")


