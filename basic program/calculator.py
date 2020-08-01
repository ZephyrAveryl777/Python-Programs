while True:
    print("-"*25)
    try :
        num1= float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except:
        print("Invalid Input")
        continue
    print("\npress 1 for addition \npres 2 for subtraction \npress 3 for multiplication \npress 4 for division \npress 5 for modulus")
    option =int(input("Enter your option: "))
    print("your option",option)
           
 
    def Addition():
        result = num1 + num2 
        return "Addition of {0} and {1} gives: {2:.5f}".format(num1, num2, result )
    def Subtraction():
        result = num1 - num2 
        return "Subtraction of {0} and {1} gives: {2:.5f}".format(num1, num2, result )
    def Multiplication():
        result = num1 * num2 
        return "Multiplication of {0} and {1} gives: {2:.5f}".format(num1, num2, result )
    def Division():
        result = num1 / num2 
        return "Division of {0} and {1} gives {2:.5f}".format(num1, num2, result )
    def Modulus():
        result = num1 % num2 
        return "Modulus of {0} and {1} gives: {2:.5f}".format(num1, num2, result )
    def default():
        return "Incorrect option, check again"
    
    switcher = {
        1: Addition,
        2: Subtraction,
        3: Multiplication,
        4: Division,
        5: Modulus
        }
    
    def switch(option):
        return switcher.get(option, default)()


    print(switch(option))
    continue
    pass
        
