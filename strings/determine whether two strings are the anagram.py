print('''
Two Strings are called the anagram if 
they contain the same characters. 
However, the order or sequence of the
characters can be different. 
''')
str1=input('Enter your first string: ').lower()
str2=input('Enter your second string: ').lower()
if len(str1)!= len(str2):
	print('both strings are not anagram.')
else:
	#sorting strings
	str1 = ''. join(sorted(str1));  
	str2 = ''. join(sorted(str2));

	if str1==str2:
		print('Both the strings are anagram.')
	else:
		print('both the strings are not anagram.')