#Python Program to compute prime factors of an integer.
n = int(input("Enter an integer: "))
i = 1
l=[]
while i <= n :
	print("Step 1:",i)
	k = 0
	if n%i == 0:
        print("Step 2:",i)
		j = 1 
		while j <= i:
			if i%j == 0:
				print("Step 3: ",i)
				k = k+1
			j=j+1
			print("Step 4:"i,j)
		if k == 2:
			print("Step 5:",i,j,k)
		    l.append(i)		
	i=i+1
print("The Prime Factors are: {}".format(l))