'''
Problem Description
The program takes a dictionary and removes a given key from the dictionary.

Problem Solution
1. Declare and initialize a dictionary to have some key-value pairs.
2. Take a key from the user and store it in a variable.
3. Using an if statement and the in operator, check if the key is present in the dictionary.
4. If it is present, delete the key-value pair.
5. If it isn’t present, print that the key isn’t found and exit the program.
6. Exit.
'''
dictionary={}
n=int(input('Enter the number of elements of the dictionary: '))
for i in range(n):
	keys=input('Enter keys: ')
	values=input('Enter values: ')
	dictionary.update({keys:values})

print(f'Inital Elements present in the dictionary is: {dictionary}')
delKey=input('Enter Key to be deleted: ')
if delKey in dictionary:
	del dictionary[delKey]
	print(f'{delKey},key is deleted')
else:
	print(f'{delKey}, Key not found.')
	exit(0)
print(f'Updated Dictioanry: {dictionary}')