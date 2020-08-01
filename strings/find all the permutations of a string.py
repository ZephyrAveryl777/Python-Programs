"""
This program can be solved by the concept of backtracking.
Fix a character in the first position 
and swap the rest of the character 
with the first character. 
Like in ABC, in the first iteration 
three strings are formed: 
ABC, BAC, and CBA by swapping A with A, 
B and C respectively.
Repeat step 1 for the rest of the characters 
like fixing second character B and so on.
Now swap again to go back to the previous position. 
E.g., from ABC, we formed ABC by fixing B again, 
and we backtrack to the previous position and swap B 
with C. So, now we got ABC and ACB.
Repeat these steps for BAC and CBA, to get all the 
permutations.
"""
# Python code to demonstrate  
# to find all permutation of 
# a given string 
# Function to swap two characters in a character array
def swap(ch, i, j):
	temp = ch[i]
	ch[i] = ch[j]
	ch[j] = temp
# Recursive function to generate all permutations of a String
def permutations(ch, curr_index=0):
	if curr_index == len(ch) - 1:
		print(''.join(ch))

	for i in range(curr_index, len(ch)):
		swap(ch, curr_index, i)
		permutations(ch, curr_index + 1)
		swap(ch, curr_index, i)
if __name__ == '__main__':
	s = input('Enter string here: ').lower()
	print(f"Permutations of the string \"{s}\" are:")
	result=permutations(list(s.upper()))