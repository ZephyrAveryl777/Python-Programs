'''
Multilevel inheritence Discription:
-----------------------------------
In Multilevel Inheritence, one can inherit from a derived class, 
thereby making this derived class the base class for the new class
'''
print(__doc__,end='')
print("-"*70)
class MusicalInstrument:
    num_of_major_keys = 12
  
class StringInstrument(MusicalInstrument):
    type_of_wood = 'Tonewood'
  
class Guitar(StringInstrument):
    def __init__(self):
        self.num_of_strings = 6
        print(f'''\nResult of MultiLevel Inheritence is: 
The guitar consists of {self.num_of_strings} strings, it is made of {self.type_of_wood} and can play {self.num_of_major_keys} keys.''')
  
guitar = Guitar()