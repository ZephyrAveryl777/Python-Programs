'''
In order to do slicing, 
use the square brackets with
the index or indices.
'''
tuples = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
 
print(f'Elements of the tuple: {tuples}') 
print(f'\nFirst Slice tuples[4:]: {tuples[4:]}')  # From index 4 to last index
 
print(f'\nSecond Slice tuples[:4]: {tuples[:4]}')  # From index 0 to 4 index
 
print(f'\nThird Slice tuples[4:7]: {tuples[4:7]}')  # From index 4(included) up to index 7(excluded)
 
print(f'\nFourth Slice tuples[1::]: {tuples[1::]}')  # Excluded First item
 
print(f'\nFifth Slice tuples[:-1]: {tuples[:-1]}')  # Excluded last item
 
print(f'\nSixth Slice tuples[:-2]: {tuples[:-2]}')  # Up to second last index(negative index)
 
print(f'\nSeventh Slice tuples[::-1]: {tuples[::-1]}')  # From last to first in reverse order(negative step)
 
print(f'\nEigth Slice tuples[::-2]: {tuples[::-2]}')  # All odd numbers in reversed order
 
print(f'\nNinth Slice tuples[-2::-2]: {tuples[-2::-2]}')  # All even numbers in reversed order
 
print(f'\nTenth Slice tuples[::]: {tuples[::]}')  # All items