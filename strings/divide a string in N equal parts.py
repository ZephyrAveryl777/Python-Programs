"""To check whether the string can be divided into N equal parts, we need to divide the length of the string by n and assign the result to variable chars.

If the char comes out to be a floating point value, we can't divide the string otherwise run a for loop to traverse the string and divide the string at every chars interval.
"""
str=input('Enter your text: ').lower()
length=len(str)
#n determines the variable that divide the string in n equal parts
n=int(input('Enter value to divide the sting equally into: '))
temp=0
chars=int(length//n)
#stores the array of string
equalStr=[]
#check whether a string can be divided into n equal parts
if length%n!=0:
	print(f'String cannot be divided into {n} equal parts.')
else:
	for i in range(0,length,chars):
		#dividing string in n equal part using substring()
		part=str[i:i+chars]
		equalStr.append(part)
	print('Equal parts of given string are: ')
for i in equalStr:  
	print(i);
