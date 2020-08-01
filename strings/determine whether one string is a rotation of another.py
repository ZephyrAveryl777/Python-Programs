'''
Algorithm
Define two string 1 and string 2.
To check whether string 2 is rotation of string 1 
then, first check the length of both the strings. 
If they are not equal, then string 2 cannot be a 
rotation of string 1.
Concatenate string 1 with itself and assign it to 
string 1.
Check the index of string 2 in string 1. 
If it exists then, string 2 is a rotation of string 1.
'''
string1=input('Enter the first string: ')
string2=input('Enter the second string: ')
if len(string1)!=len(string2):
	print('second string is not a ratation of first string!')
else:
	try:
		#Concatenate first string with itself and store it in string1
		string1=string1+string2
		#check whether string2 is present in string1
		if string1.index(string2):
			print('Second string is a rotation of first string')
	except ValueError:
		print('Second string is not a rotation of first string')