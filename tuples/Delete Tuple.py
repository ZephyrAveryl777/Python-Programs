test=[]
n=int(input('Enter size of tuple: '))
for i in range(n):
	data=input('Enter elements of tuple: ')
	test.append(data)
test=tuple(test)
print(f'elements in tuple: {test}')
del test #Tuple deleted completely 
#hence cant be accessed again

