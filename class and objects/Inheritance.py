'''
Single Inheritence Discription: 
-------------------------------
Single inheritance enables a derived class to inherit properties
and behavior from a single parent class. It allows a derived class
to inherit the properties and behavior of a base class, thus enabling 
code reusability as well as adding new features to the existing code.
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
        print(f'''\nResult of Single Inheritance: This MacBook was manufactured in {self.year_of_manufacture}, by {self.manufacturer}''')
  
macbook = MacBook()
macbook.manufacture_details()
