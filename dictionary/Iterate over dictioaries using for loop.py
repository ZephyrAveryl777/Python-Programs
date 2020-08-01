d1 = {'Canada': 100, 'Japan': 200, 'Germany': 300, 'Italy': 400}
 
# Example 1 Print only keys
print("*" * 10)
for x in d1:
    print(x)
 
# Example 2 Print only values
print("*" * 10)
for x in d1:
    print(d1[x])
 
# Example 3 Print only values
print("*" * 10)
for x in d1.values():
    print(x)
 
# Example 4 Print only keys and values
print("*" * 10)
for x, y in d1.items():
    print(x, "=>", y)
 