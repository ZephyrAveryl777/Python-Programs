'''
mro stands for Method Resolution Order. 
It returns a list of types the class is 
derived from, in the order they are searched 
for methods'''
print(__doc__)
print('\n'+'-'*35+ 'Method Resolution Order'+'-'*35)
class A(object):
    def dothis(self):
        print('From A class')
 
 
class B1(A):
    def dothis(self):
        print('From B1 class')
    pass
 
 
class B2(object):
    def dothis(self):
        print('From B2 class')
    pass
 
 
class B3(A):
    def dothis(self):
        print('From B3 class')
 
 
# Diamond inheritance
class D1(B1, B3):
    pass
 
 
class D2(B1, B2):
    pass
 
 
d1_instance = D1()
d1_instance.dothis()
print(D1.__mro__)
 
d2_instance = D2()
d2_instance.dothis()
print(D2.__mro__)