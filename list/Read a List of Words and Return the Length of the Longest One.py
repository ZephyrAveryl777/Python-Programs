"""
Problem Description
The program takes a list of words and returns the word with the longest length.
Problem Solution
1. Take the number of elements in the list and store it in a variable.
2. Accept the values into the list using a for loop and insert them into the list.
3. First assume that the first element is the word with the longest length.
4. Then using a for loop and if statement, compare the lengths of the words in the list with the first element.
5. Store the name of the word with the longest length in a temporary variable.
6. Display the word with the longest length
7. Exit.
"""
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input(f"Enter element at position {x}: ")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print(f"The word with the longest length is: {temp}")