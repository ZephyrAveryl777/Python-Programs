#Python Program to take the temperature in Celsius and convert it to Fahrenheit.
while 1:
    try:
        #a=Celsius= float(input("Enter the temperature in Celcius: "))
        print("----------------------------------------------------------------------")
        print("*                                                                    *")
        print("*       Welcome  to the Temperature Converter - המרת טמפרטורה      *")
        print("*                                                                    *")
        print("----------------------------------------------------------------------")
        #b=Fahrenheit = float(input("Enter the temperature in  Farenheit: "))
    except:
        print("Invalid Input")
        continue
    print("\npress 1 for Converting Celsius to Fahrenheit \npres 2 for Converting Fahrenheit to Celsius ")

    option =int(input("\nEnter your option: "))
    print("your have selected the option",option)

    def Celsius():
    	#Fahrenheit = float((Celsius * 1.8) + 32)
                a=Celsius= float(input("\nEnter the temperature in Celcius: "))
                c = float(a *1.8)
                Fahrenheit = float(c +32)
                return "The given Celsius {0}, in Fahrenheit  it is : {1} ".format(a,round(Fahrenheit,4))

    def Fahrenheit():
    	#Celsius = float((Fahrenheit - 32) / 1.8)
                b=Fahrenheit = float(input("\nEnter the temperature in  Farenheit: "))
                c = float( b - 32)
                Celsius = float( c / 1.8)
                return "The given Fahrenheit {0}, in Celsius is : {1} ".format(b,round(Celsius,4))

    def default():
    	return "Invalid option - default command executed!, Please check again."

    switcher = {
         1: Celsius,
         2: Fahrenheit
         }

    def switch(option):
    	return switcher.get(option,default)()

    print(switch(option))
    choice = input("\nDo you wish to continue if so press y else n: ")	
    if choice == "y" :
            print("-----------------------------------------------------")
            continue
    elif choice == "n" :
            print("\nThank you for using the program, hope you enjoyed it, Pls do visit again.")
            print("-----------------------------------------------------------------------")
            break
    else :
            print("\nUnable to determine whether to continue or stop the execution of the program. Hence program aborted ! Restart the program.")
            print("-------------------------------------------------------------------------------")
            break