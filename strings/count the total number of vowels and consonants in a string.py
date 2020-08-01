print('''
Vowels are A,E,I,O,U 
any alphabet other than
this is consonants
''')
Vowels_count=0
consonants_count=0
#Converting entire string to lower case to reduce the comparisons  
str=input('Enter your text here: ').lower()
for i in range(0,len(str)):
	#check whether a character is a Vowel
	if str[i] in ('a','e','i','o','u'):
		Vowels_count = Vowels_count+1
	elif str[i]>='a' and str[i]<='z':
		consonants_count=consonants_count+1

print(f'total number of vowels are {Vowels_count} \ntotal number of consonants are: {consonants_count} ')