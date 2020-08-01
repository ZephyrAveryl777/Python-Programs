'''
You can use dict() method to convert 
tuple into dictionary.
'''
test = (('America', 27), ('Canada', 25), ('Japan', 5), ('Italy', 0))
 
dict1 = dict(i for i in test)
dict2 = dict(map(reversed, test))
dict3 = dict(i[::1] for i in test)
print(f'\nElements of the tuple: {test}') 
print(f'\nDictionary using dict_method: {dict1}')
print(f'\nDictionary using dict_map method: {dict2}')
print(f'\nDictionary using dict_item_iteration: {dict3}')