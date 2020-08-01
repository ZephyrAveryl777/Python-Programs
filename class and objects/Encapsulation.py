'''
Discription:
------------
The wrapping up of data and functions into a single unit (called class) is known as encapsulation. 
Data encapsulation is the most striking feature of a class. The data is not accessible to the outside 
world, and only those functions, which are wrapped in the class, can access it. These functions provide 
the interface between the object’s data and the program. This insulation of the data from direct access 
by the program is called data hiding or information hiding.
'''
print(__doc__,end="")
print('-'*100)
class Encapsulation:
	a = __name = None

	def __init__(self,name):
		self.__name = name

	def get_name(self):
		return self.__name

private_obj= Encapsulation('The Rock')
print(f'''
Before Encapsulation the output is: {Encapsulation.a}
After Encapsulation the output is: {private_obj.get_name()}
''')
