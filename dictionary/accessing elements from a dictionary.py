#Dictionary:
Dict={1:'Hi','name': 'Hello',3:'how are you?'}

#accessing a element using key
print(f'Accessing a element using a key: {Dict["name"]}')

#accessing a element using key
print(f'Accessing an element using a key: {Dict[1]}')

#accessing a element using get()
print(f'Accessing an element using get(): {Dict.get(3)}')

# Nested Dictionary
Dict={'Dict1': {1:'Hey'},
		'Dict2': {1: 'What\'s up?',2:'Yo, let\'s party'}
	}
print(f'Nested Dictionary: {Dict}')

#accessing a element using key
print(f'Accesing an element in the Nested Dictionary: {Dict["Dict1"]}')
print(f'Accesing an element in the Nested Dictionary: {Dict["Dict2"][1]} ')
print(f'Accesing an element in the Nested Dictionary: {Dict["Dict2"][2]} ')