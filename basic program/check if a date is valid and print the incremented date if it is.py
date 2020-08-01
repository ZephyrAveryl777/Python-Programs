while True:
	date = input("Enter the date in the format dd/mm/yy : ") # input the date in the given format
	dd,mm,yy=date.split('/') # spliting the date values 
	dd=int(dd)
	mm=int(mm)  #values from the date in the given format
	yy=int(yy)
	if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12): # months which have 31 days 
	    max=31
	elif(mm==4 or mm==6 or mm==9 or mm==11): # months which have 30 days
	    max=30
	elif(yy%4==0 and yy%100!=0 or yy%400==0): # if the year is leap year
	    max=29
	else:
	    max=28
	if(mm<1 or mm>12): # check the validity of month
	    print("Date is invalid.")
	elif(dd<1 or dd>max): # check the validity of date 
	    print("Date is invalid.")
	elif(dd==max and mm!=12): # incrementing the month (except month = 12, ie December), only if date is last day of the month
	    dd=1
	    mm=mm+1
	    print("The incremented date is: {0}/{1}/{2}".format(dd,mm,yy))
	elif(dd==31 and mm==12): # incrementing the year if the day and the month are the last (31st December)
	    dd=1
	    mm=1
	    yy=yy+1
	    print("The incremented date is: {0}/{1}/{2} ".format(dd,mm,yy))
	else: # in any ordinary date other than the above two conditions
	    dd=dd+1
	    print("The incremented date is: {0}/{1}/{2}".format(dd,mm,yy))
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