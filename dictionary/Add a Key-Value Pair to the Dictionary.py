'''
Problem Description
The program takes a key-value pair and 
adds it to the dictionary.

Problem Solution
1. Take a key-value pair from the user and 
store it in separate variables.
2. Declare a dictionary and initialize 
it to an empty dictionary.
3. Use the update() function to add the 
key-value pair to the dictionary.
4. Print the final dictionary.
5. Exit.
'''
key=int(input('Enter the key to be added: '))
value=int(input('Enter the value for the key to be added: '))
d={}
d.update({key:value})
print(f'Updated dictionary is: {d}')
