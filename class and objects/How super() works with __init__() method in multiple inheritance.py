'''
super support cooperative multiple inheritance in a dynamic execution 
environment. This use case is unique to Python and is not found in 
statically compiled languages or languages that only support single inheritance.
'''
print(__doc__)
print('\n'+'-'*35+'Super() working'+'-'*35)
class F:
    def __init__(self):
        print('F class%s' % super().__init__)
        super().__init__()
 
 
class G:
    def __init__(self):
        print('G class%s' % super().__init__)
        super().__init__()
 
 
class H:
    def __init__(self):
        print('H class%s' % super().__init__)
        super().__init__()
 
 
class E(G, H):
    def __init__(self):
        print('E class%s' % super().__init__)
        super().__init__()
 
 
class D(E, F):
    def __init__(self):
        print('D class%s' % super().__init__)
        super().__init__()
 
 
class C(E, G):
    def __init__(self):
        print('C class%s' % super().__init__)
        super().__init__()
 
 
class B(C, H):
    def __init__(self):
        print('B class%s' % super().__init__)
        super().__init__()
 
 
class A(D, B, E):
    def __init__(self):
        print('A class%s' % super().__init__)
        super().__init__()
 
 
a = A()
print(a)