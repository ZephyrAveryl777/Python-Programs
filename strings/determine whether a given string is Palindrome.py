print('''
A string is said to be palindrome if it reads 
the same backward as forward. For e.g. "AKA" string 
is a palindrome because if we try to read it from 
backward, it is same as forward. One of the approach 
to check this is iterate through the string till 
middle of string and compare a character from back 
and forth.
 ''')
string=input('Enter string here: ')
flag=1
#converts the given string into lowercase
string=string.lower()
#Iterate the string forward and backward, compare one character at a time   
#till middle of the string is reached  
for i in range(len(string)//2):
	if string[i]!=string[len(string)-i-1]:
		flag=0
		break

if flag:
	print(f'Given string \" {string} \" is a palindrome')
else:
	print(f"Given string \" {string} \" is not a palindrome")
