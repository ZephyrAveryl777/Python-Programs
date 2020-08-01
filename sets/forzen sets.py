'''
Frozen sets in Python are 
immutable objects that only 
support methods and operators 
that produce a result without 
affecting the frozen set or 
sets to which they are applied. 
While elements of a set can be 
modified at any time, elements 
of the frozen set remain the same a
fter creation.
If no parameters are passed, 
it returns an empty frozenset.
'''
# Python program to demonstrate differences 
# between normal and frozen set 
  
# Same as {"a", "b","c"} 
normal_set = set(["a", "b","c"]) 
  
print(f"Normal Set elements are: {normal_set}")   

# A frozen set 
frozen_set = frozenset(["e", "f", "g"]) 
print(f"\nFrozen Set elements are: {frozen_set}") 
