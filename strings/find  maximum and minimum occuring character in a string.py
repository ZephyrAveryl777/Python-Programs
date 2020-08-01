string=input('Enter string here: ')
frequncy = [None]*len(string)
minChar=string[0]
maxChar=string[0]

#count each word in given string and store in frequncy list
for i in range(len(string)):
	frequncy[i]=1
	for j in range(i+1,len(string)):
		if string[i]==string[j] and string[i]!='' and string[i]!='0':
			frequncy[i]+=1
			#Set string[j] to 0 to avoid printing visited character
			string=string[:j]+'0'+string[j+1:]
#determine minimum and maximum occuring character
min=max=frequncy[0]
for i in range(len(frequncy)):
	#if min is greater than frequncy of a character
	#then, store frequncy in min and corresponding character in minChar
	if min>frequncy[i] and frequncy[i]!='0':
		min=frequncy[i]
		minChar=string[i]
		#if max is less than frequncy of a character
		#then store frequncy in max and corresponding character in maxChar
		if max<frequncy[i]:
			max=frequncy[i]
			minChar=string[i]

print(f'Minimum occuring character: {minChar}')
print(f'maximum occuring character: {maxChar}')