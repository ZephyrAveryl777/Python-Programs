while True:
	year=int(input("Enter the year to be checked: "))
	if (year%4==0 and year%100 != 0 or year%400 == 0):
		print("The year {} is a leap year".format(year))
	else:
		print("The year {} is not a leap year".format(year))

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
