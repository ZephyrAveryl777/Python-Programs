"""
Decimal System: The most widely used number system is decimal system. This system is base 10 number system. 
In this system, ten numbers (0-9) are used to represent a number.
Binary System: Binary system is base 2 number system. 
Binary system is used because computers only understand binary numbers (0 and 1).
Octal System: Octal system is base 8 number system.
Hexadecimal System: Hexadecimal system is base 16 number system.
This program is written to convert decimal to binary, octal and hexadecimal.
""" 
while 1: 
	dec = int(input("Enter a decimal number: "))  
	print(bin(dec),"in binary.")  
	print(oct(dec),"in octal.")  
	print(hex(dec),"in hexadecimal.") 
	continue