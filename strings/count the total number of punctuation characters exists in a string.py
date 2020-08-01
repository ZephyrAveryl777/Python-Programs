print('''
In this program, all the subsets of the string
need to be printed. The subset of a string is
the character or the group of characters that are present
inside the string. For example, all possible subsets of
a string "FUN" will be F, U, N, FU, UN, FUN.
''')
count=0
str=input('Enter your statement here: ')
for i in range(0,len(str)):
	#check whether given character is a punctuation mark.
	if str[i] in ('!',',','\'','/',',','.',':','-','?'):
		count=count+1

print(f'Total number of punctuation charaters existing in string are: {count}')
