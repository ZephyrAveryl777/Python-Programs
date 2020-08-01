# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
        'B' : {1 : 'Geeks', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 
  
# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 
  
# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 

#using method POP()
#creating a Dictionary
Dict={1:'Hi','name': 'Hello',3:'how are you?'}
print(f'\nDictionary before poping: {Dict}')

#Deleting a key using pop() method
pop_element=Dict.pop(1)
print(f'\nDictionary after Deletion: {Dict}')
print(f'\nValue associated to poped key is: {pop_element}')

#using popitem() method
Dict={1:'Hi','name': 'Hello',3:'how are you?'}
print(f'\nDictionary before poping: {Dict}')

#Deleting arbitray key using popitem()
pop_element=Dict.popitem()
print(f'\nDictionary after deletion: {Dict}')
print(f'\nThe arbitrary pair returned is: {pop_element}')

#using clear() method
Dict={1:'Hi','name': 'Hello',3:'how are you?'}
print(f'\nDictionary before poping: {Dict}')

#Deleting entire Dictionary
Dict.clear()
print(f'\nDeleting Entire Dictionary: {Dict}')