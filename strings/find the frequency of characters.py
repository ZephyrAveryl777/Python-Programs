"""
To accomplish this task, we will maintain an array called freq with same size of the length of the string. Freq will be used to maintain the count of each character present in the string. Now, iterate through the string to compare each character with rest of the string. Increment the count of corresponding element in freq. Finally, iterate through freq to display the frequencies of characters."""
string=input('Enter string here: ').lower()
freq = [None] * len(string);  
   
for i in range(0, len(string)):  
    freq[i] = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j]):  
            freq[i] = freq[i] + 1;  
              
            #Set string[j] to 0 to avoid printing visited character  
            string = string[ : j] + '0' + string[j+1 : ];  
              
#Displays the each character and their corresponding frequency  
print("Characters and their corresponding frequencies");  
for i in range(0, len(freq)):  
    if(string[i] != ' ' and string[i] != '0'):  
        print(f'frequency of {string[i]} is: {str(freq[i])}')