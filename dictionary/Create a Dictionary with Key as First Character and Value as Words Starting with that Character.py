'''
Problem Description
The program takes a string and creates a dictionary with key as first character and value as words starting with that character.

Problem Solution
1. Enter a string and store it in a variable.
2. Declare an empty dictionary.
3. Split the string into words and store it in a list.
4. Using a for loop and if statement check if the word already present as a key in the dictionary.
5. If it is not present, initialize the letter of the word as the key and the word as the value and append it to a sublist created in the list.
6. If it is present, add the word as the value to the corresponding sublist.
7. Print the final dictionary.
8. Exit.
'''
text=input('Enter string: ')
l=text.split()
dictionary={}
for word in l:
	if word[0] not in dictionary.keys():
		dictionary[word[0]]=[]
		dictionary[word[0]].append(word)
	else:
		if word not in dictionary[word[0]]:
			dictionary[word[0]]=[]
			dictionary[word[0]].append(word)
for keys,values in dictionary.items():
	print(f'{keys}:{values}')
