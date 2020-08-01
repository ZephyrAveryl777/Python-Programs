#1) Creating set
primes={3,5,7,9,11,13}
print(primes.__doc__)
print('\n1. Creating set: ')
print('-'*15)
print(f'The type of elements created are: {type(primes)}')
print(f'Elements of the set are: {primes}')

# 2) Creating set with constructor
print('\n2. Creating set with constructor: ')
print('-'*35)
unique=set("hihellohowareyou?");
print(f'Printing the elements of the set: {unique}')

# 3) Creating empty set
print('\n3. Creating empty set: ')
print('-'*25)
empty={}
print(f'If set is declared as setName = {{}} then its type is : {type(empty)}')
empty=set()
print(f'If set is declared as setName = set() then its type is : {type(empty)}')

#4) Creating set from List
print('\n4. Creating set from List: ')
print('-'*25)
primesList=[3,5,7,11,13,17];
print(f'Elements of the list are: {primesList}, their type is: {type(primesList)}')
primeSet=set(primesList)
print(f'Elements of the set are: {primeSet},their type is: {type(primeSet)}')

# 5) Creating set from tuple
print('\n5. Creating a set from tuple: ')
print('-'*25)
p=(3,5,7,11,13);
print(f'Elements of the tuple are: {p}, their type is: {type(p)}')
primes=set(p);
print(f'Elements of the set are: {primes}, their type is: {type(primes)}')

# 6) Accessing values in Set
Primes = {3, 5, 7, 11, 13};
print('\n6. Accessing values in Set: ')
print('-'*25)
print(f"Elements of the set: {Primes}") 
try:
	Primes[1];
except:
	print(f'''Trying to access set elements Primes[1]: You cannot access items in a set by referring to an index, since sets are 
unordered the items has no index.''')
# uncommenting this throw error

#7) Using Add method
primes={3,5,7,11};
print('\n7. Using Add Method: ')
print('-'*25)
print(f'Elements of set are: {primes}')
primes.add(19);
print(f'After adding elements of the set: {primes}')

# 8) Using update method
print("\n8. Using update method: ")
print('-'*25)
plist=[12,14,15,16];
print(f'Elements of the list are: {plist}, their type is: {type(plist)}')
print(f'Elements of the set before upadting are: {primes}')
primes.update(plist);
print(f'Elements after updating the list are: {primes}, their type is {type(primes)}')

#9) Using discard
print(f'\n9. Using Discard: ')
print('-'*15)
primes={3, 5, 'Zephr', 7, 11, 12, 14, 15, 16, 19};
print(f'Elements of the set before discarding are: {primes}')
primes.discard("Zephr")
print(f'Elements of the set after using .discard(" ") method are : {primes}')

# 10) Using remove
print('\n10. Using remove(): ')
print('-'*20)
primes = {3, 5, 7, 11, 12, 14, 15, 16, 19}
print(f'Elements of the set before using remove() are: {primes}')
primes.remove(11)
print(f'Elements of the set after using remove() are: {primes}')

# 11) Union operation on sets
primes1={3,5,7,11}
print('\n11. Union operation on set: ')
print('-'*25)
print(f'Elements of first set are: {primes1}')
primes2={3,5,7,11,13,17,19}
print(f'Elements of second set are: {primes2}')
primes=primes1 | primes2
print(f'Elements of the set after using union operation are: {primes}')

# 12) Intersection operation on Sets
print('\n12. Intersection operation on Set: ')
print('-'*35)
prime1={3,5,7,11};
print(f'Elements of first set are : {prime1}')
prime2={3,5,7,11,13,17,19}
print(f'Elements of second set are: {prime2}')
primes=prime1 &  prime2
print(f'Elements of the set after using intersection operation are: {primes}')

# 13) Difference operation on sets
print(f'\n13. Difference operation on sets: ')
print('-'*35)
prime2={3,5,7,11,13,17,19}
print(f'Elements of first set are: {prime2}')
prime1={3,5,7,11};
print(f'Elements of second set are: {prime1}')
primes=prime2-prime1
print(f'Elements of the set after using Difference operation are: {primes}')

# 14) Symmetric difference
print(f'\n14. Symmetric Difference: ')
print('-'*25)
prime2={3,5,7,11,13,17,19}
print(f'Elements of first set are: {prime2}')
prime1={3,5,7,11,91,101}
print(f'Elements of second set are: {prime1}')
primes=prime2 ^ prime1
print(f'Elements of the set after Symmetric difference are: {primes}')

# 15) Compare two sets
print(f'\n15. compare two sets: ')
print('-'*25)
prime1={3,5,7,11,91,101};
print(f'Elements of first set are: {prime1}')
prime={3,5,7,11,91,101};
print(f'Elements of second set are: {prime2}')
test=prime==prime1
test1=prime2<prime1
print(f'After comparing both the sets are equal : {test}, second set is less than first one: {test1}')
print('''(Note! comparison operators always returns Boolean.)''') 

#16) Membership test on sets
print(f'\n16. Membership test on sets: ')
print('-'*25)
prime1={3,5,7,11,91,101}
print(f'Elements of the set are: {primes}')
test= 3 in prime1
print(f'After checking whether an element  belongs to set: {test}')
print('''(Note! Membership operators always returns Boolean.)''')

# 17) Iterating on set
print(f'\n17. Iterating on set: ')
print('-'*25)
primes={3,5,7,11,91,101};
print(f'Elements of set are: ')
for prime in primes:
    print(prime)

# 18) Clearing a set
print('\n18. Clearing a set: ')
print('-'*20)
prime1= {3, 5, 101, 7, 11, 91}
print(f'Elements of the set are: {prime1}, their type is: {type(prime1)}')
prime1.clear()
print(f'Elements of the set after clearing are: {prime1}')

#19) interesting problem
print(f'\n19. Converting a list of numbers to set: ')
print('-'* 35)
number = [1,2,3,4,5,2,3,4,7,8,9,8,12,13,14,14,19]
print(f'Elements of the list are: {number}, their type is: {type(number)}')
print (f'''After converting the elements of list ot set they are: {set(number)}, 
	their type is {type(number)}''')

#20) taking input from user
print(f'\n20. Taking input from user: ')
print('-'* 25)
a=set()
n=int(input('Enter size of set: '))
for i in range(n):
	element=int(input('Enter elements of set: '))
	a.add(element)
print(f'Elemnets of the set are: {a}')

