'''
When calling super to resolve to a parent's version of a class-method, 
instance method, or static-method, we want to pass the current class 
whose scope we are in as the first argument, to indicate which parent's 
scope we're trying to resolve to, and as a second argument the object of 
interest to indicate which object we're trying to apply that scope to.
'''
print(__doc__)
print('\n'+'-'*35+'Super() within a class method'+'-'*35)
class A(object):
	@classmethod
	def name(self,employee):
		print('Employee Name: ',employee)

class B(A):
	@classmethod
	def name(self,employee):
		super(B,self).name(employee)

B.name('Will Smith')