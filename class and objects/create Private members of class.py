'''
Discription:
------------
If the name of a Python function, class method, or attribute 
starts with (but doesnot end with) two underscores, its 
private; everything else is public.Example: __<name> is private <name> 
(name could be Class, method,attribute)
'''
print(__doc__,end='')
print('-'*45)
class Test(object):
	__private_var=100
	public_var=200

	def __private_function(self):
		print('Private Function')

	def public_function(self):
		print('Public Function')
		print(self.public_var)

	def call_private(self):
		self.__private_function() #calling the private function.
		print(self.__private_var) #calling the private variable. 

t=Test()
print(f'Dealing with the: {t.call_private()}')
print(f'Dealing with the: {t.public_function()}')

'''
print(f'Dealing with the: {t.__private_function()}')
AttributeError: 'Test' object has no attribute '__private_function'
'''