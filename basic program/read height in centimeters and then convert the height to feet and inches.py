while 1: 
	cm = int(input("Enter the height in centimeter: "))
	inches = 0.394 * cm
	feet = 0.0328 * cm
	print("The length in inches: ",round(inches, 2))
	print("The length in feet: ",round(feet,2))
	option=input("\nDo you wish to stop the program then type n, if not pres y :")
	print("---------------------------------------------------------------------")
	if option == "n" :
		break
	elif option == "y" :
		continue
	else :
		print("Unable to determine wether to continue execution or not!, Please check again! ")
		print("-------------------------------------------------------------------------------")
		break