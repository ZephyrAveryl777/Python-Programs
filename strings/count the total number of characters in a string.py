string=input('Enter string here: ')
count=0
#counts each character except space
for i in range(0,len(string)):
	if string[i]!= ' ':
		count+=1
#Displays the total number of characters present in the given string  
print(f'Total number of chatracters in a string: {count}')