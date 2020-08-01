string=input('Enter string here: ')
#stores the reverse of given string
reversed_string=''
#Iterate through the string from last and add each character to variable reversedStr  
for i in range(len(string)-1,-1,-1):
	reversed_string=reversed_string+string[i]

print(f'Original String is: \" {string} \" ')
print(f'Reverse of given string is: \" {reversed_string} \" ')