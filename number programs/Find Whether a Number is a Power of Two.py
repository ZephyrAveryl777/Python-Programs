def ispoweroftwo(n):
	"""Return True if n is power of two."""
	if n<=0:
		return False
	else:
		return n & (n-1) == 0
n = int(input("Enter a number: "))
if ispoweroftwo(n):
	print(f"{n} is a power of two.")
else:
	print(f"{n} is not a power of two.")