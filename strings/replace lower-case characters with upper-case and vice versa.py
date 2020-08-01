string=input('Enter string here: ')
new_string=' '
for i in range(0,len(string)):
	#check for lower case character
	if string[i].islower():
		#convert it into uppercase using upper() function
		new_string = new_string+string[i].upper()
		#checks for upper case character
	elif string[i].isupper():
		#convert it into lower case using lower() function
		new_string = new_string+string[i].lower()
	else:
		new_string = new_string+string[i]
print(f'String after case conversion:{new_string}')