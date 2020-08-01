#Problem Description
#The program computes simple interest given the principle amount, rate and time.
principle = float(input("Enter the principle amount: "))
time = int(input("Enter the time(years): "))
rate = float(input("Enter the rate: "))
simple_interest= (principle*time*rate)/100
print("""------------------------------------
The simple interest is : {} """.format(simple_interest))