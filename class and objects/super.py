'''
Discription:
------------
In a class hierarchy with single inheritance, 
super can be used to refer to parent classes 
without naming them explicitly, thus making 
the code more maintainable. This use closely 
parallels the use of super in other programming 
languages.
'''
print(__doc__,end="")
print('\n'+'-'*35+'Super'+'-'*35)
class A(object):
	def __init__(self,profession):
		print(profession)

class B(A):
	def __init__(self):
		print('John Doe ',end="")
		super().__init__('Developer')

b=B()

