'''
During unpacking of 
tuples items value assigned to variables.
'''
print('Unpacking of tuple items ')
countrylist = ("America", "Canada", "Japan", "Italy")
usa, can, jap, itl = countrylist
print(f'Elements of the tuple are: {countrylist}')
print(f'\ncountrylist: usa =>{usa}')
print(f'countrylist: can =>{can}')
print('-'*20)
print('Packing of tuple items: ')
#create a tuple
l = [(1,2), (3,4), (8,9)]
print(f'Elements of tuple: {tuple(l)}')
print (tuple((zip(*l))))
