'''
The sorted() method is used to sort items of a dictionary.
'''
d1 = {'Canada': 100, 'Japan': 200, 'Germany': 300, 'Italy': 400} 
print('-'*15)
for key in sorted(d1):
    print("%s: %s" % (key, d1[key]))
print('-'*15)

'''
Sorting a Dictionary by value'''
d1 = {'Canada': 300, 'Japan': 400, 'Germany': 100, 'Italy': 200}
for x in sorted(d1, key=d1.get):
    print(f'{x} : {d1[x]}')