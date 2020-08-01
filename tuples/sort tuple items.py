'''
You can use sorted() method to sort items of tuple. 
But it should be of homogeneous data type:
'''
test1 = ("England", "Canada", "Japan", "Italy","America")
test2 = (27, 25, 5, 0)
test3 = (('America', 27),('Canada', 25),('Japan', 5), ('Italy', 0))
print(f'\nElements of the first tuples: {test1}')
print(f'\nElements of the second tuples: {test2}')
print(f'\nElements of the third tuples: {test3}') 
print(f'\nSorting first tuple: {sorted(test1)}')
print(f'\nSorting second tuple: {sorted(test2)}')
print(f'\nSorting third tuple: {sorted(test3)}')