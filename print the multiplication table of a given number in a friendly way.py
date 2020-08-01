#Python Program to print the table of a given number.
while 1: 
	n=int(input("Enter the number to print the tables for: "))
	for i in range(1,21):
	    print(n,"X",i,"= ",n*i)
	option = input("\nDo you wish to continue if so press y else n: ")	
	if option == "y" :
		print("-----------------------------------------------------")
		continue
	elif option == "n" :
		print("\nThank you using the program, hope you enjoyed it, Pls do visit again.")
		print("-----------------------------------------------------------------------")
		break
	else :
		print("\nUnable to determine whether to continue or stop the executionnof the program.")
		print("-------------------------------------------------------------------------------")
		break
