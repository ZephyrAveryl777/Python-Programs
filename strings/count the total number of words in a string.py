sentence = input('Enter string here: ')  
wordCount = 0;  
   
for i in range(0, len(sentence)-1):  
    #Counts all the spaces present in the string  
    #It doesn't include the first space as it won't be considered as a word  
    if(sentence[i] == ' ' and sentence[i+1].isalpha() and (i > 0)):  
        wordCount = wordCount + 1;  
          
  
#To count the last word present in the string, increment wordCount by 1  
wordCount = wordCount + 1;  
   
#Displays the total number of words present in the given string  
print("Total number of words in the given string: " + str(wordCount));  
