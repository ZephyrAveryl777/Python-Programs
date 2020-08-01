'''
Multiple inheritence Discription: 
---------------------------------
Multiple inheritance is a feature of some object-oriented computer programming languages 
in which an object or class can inherit characteristics and features from more than one 
parent object or parent class.
'''

print(__doc__,end="")
print('-'*35)
class Apple:
    manufacturer = 'Apple Inc'
    contact_website = 'www.apple.com/contact'
    name = 'Apple'
 
    def contact_details(self):
        print('Contact us at ', self.contact_website)
 
class MacBook(Apple):
    def __init__(self):
        self.year_of_manufacture = 2018
 
    def manufacture_details(self):
    	pass
        #print(f'''\nResult of Single Inheritance: This MacBook was manufactured in {self.year_of_manufacture}, by {self.manufacturer}''')
  
macbook = MacBook()
macbook.manufacture_details()
class OperatingSystem:
    multitasking = True
    name = 'Mac OS'
 
class MacTower(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print(f'''\nResult of Multiple Inheritence is: Multitasking system''',end="")
        # if there are two superclasses with the same attribute name
        # the attribute of the first inherited superclass will be called
        # the order of inhertence matters
        print(f': Name: {self.name}')
 
mactower = MacTower()
