'''
Problem Description
The program takes a dictionary and multiplies all the items in the dictionary.

Problem Solution
1. Declare and initialize a dictionary to have some key-value pairs.
2. Initialize a variable that should contain the total multiplied value to 1.
3. Use the for loop to traverse through the values of the dictionary.
4. Then multiply all the values in the dictionary against each other.
5. Print the total multiplied value.
6. Exit.
'''
dictionary={}
n=int(input('Enter the length of the dictionary: '))
for i in range(n):
	key=input('Enter the key: ')
	value=int(input('Enter the value: '))
	dictionary.update({key:value})	

print(f'Elements of the dictionary are: {dictionary}')
total=1
for i in dictionary:
	total=total*dictionary[i]
print(f'The multiplication total of the dictionary elements are: {total}')
