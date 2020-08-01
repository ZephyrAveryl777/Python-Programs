#Python Program to find the sum of series: 1 + 1/2 + 1/3 + ….. + 1/N.
""""Problem Solution
1. Take in the number of terms to find the sum of the series for.
2. Initialize the sum variable to 0.
3. Use a for loop ranging from 1 to the number and find the sum of the series.
4. Print the sum of the series after rounding it off to two decimal places.
5. Exit.
"""
n=int(input("Enter the number of terms in the series: "))
sum=0

print("the sum of series: ", end = " ")
for i in range(1,n+1):
             print(f"1/{i}",sep=" ",end=" ")
             if i<n:
                   print("+ ",sep=" ",end=" ")
             sum=sum+(1/i)   
print(f" =  {round(sum,3)}")
print()
