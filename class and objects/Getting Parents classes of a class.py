class A(object):
	pass

class B(object):
	pass

class C(A,B):
	pass

print(f'Parent Classes are: {C.__bases__}')