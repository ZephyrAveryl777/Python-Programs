'''
Problem Description:
-------------------
The program copies the contents of 
one file and writes it into another
'''
with open('H://python programs//file handling//sample.txt') as f:
	with open("H://python programs//file handling//output.txt","w") as f1:
		for line in f:
			f1.write(line)

			 