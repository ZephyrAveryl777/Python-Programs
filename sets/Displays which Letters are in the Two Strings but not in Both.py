'''
Problem Description
The program takes two strings and displays which
letters are in the two strings but not in both.

Problem Solution
1. Enter two input strings and store it in separate variables.
2. Convert both of the strings into sets and find which of the 
letters are in the two strings but not in both.
3. Store the letters in a list.
4. Use a for loop to print the letters of the list.
5. Exit.
'''
string1=input('Enter first string: ')
string2=input('Enter second string: ')
a=list(set(string1)^set(string2))
print('The letters are: ')
for i in a:
	print(i)