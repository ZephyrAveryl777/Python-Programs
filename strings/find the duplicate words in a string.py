"""
To find the duplicate words from the string, we first split the string into words. We count the occurrence of each word in the string. If count is greater than 1, it implies that a word has duplicate in the string.
"""
string=input('Enter string here: ').lower()
word=string.split(' ')
print('duplicate words in a given string: ')
for i in range(len(word)):
	count=1
	for j in range(i+1,len(word)):
		if word[i]==word[j]:
			count+=1
			word[j]='0'
	#displays the duplicate word if count is greater than 1
	if count>1 and word[i]!='0':
		print(word[i])