'''
index() method to get first 
occurrence of the specified value in the tuple. 
Best practice is to use this method after 
determination of item exist in tuple, otherwise 
this will raise an exception.
'''
test = ("Canada", "America", "Canada", "Japan", "Italy", "Canada")

print(f'Elements of tuple: {test}')

idx = test.index("Japan")
 
print(idx)
 
idx = test.index("Canada")
 
print(idx)
 
if "Brazil" in test:
    idx = test.index("Brazil")
    print(idx)