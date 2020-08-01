"""
all the subsets of the string need to be printed. 
The subset of a string is the character or the group 
of characters that are present inside the string. 
For example, all possible subsets of a string 
"FUN" will be F, U, N, FU, UN, FUN.
"""
string=input('Enter string: ')
result=[] # to hold all the formed substring
# this loop maintains the starting characters
for i in range(len(string)):
	for j in range(i,len(string)):
		result.append(string[i:(j+1)])

#prints all the subset
print(f'all subsets for given string \"{string}\" are: ')
for i in result:
	print(list(i.split(",")))