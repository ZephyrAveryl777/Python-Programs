#Checks for the largest common prefix  
def lcp(s, t):  
  n = min(len(s),len(t));  
  for i in range(0,n):  
    if(s[i] != t[i]):  
      return s[0:i];  
  else:  
    return s[0:n];  
   
str = input('Enter string here: ') 
lrs="";  
n = len(str);  
for i in range(0,n):  
  for j in range(i+1,n):  
    #Checks for the largest common factors in every substring  
    x = lcp(str[i:n],str[j:n]);  
        #If the current prefix is greater than previous one   
        #then it takes the current one as longest repeating sequence  
    if(len(x) > len(lrs)):  
      lrs=x;    
print("Longest repeating sequence: "+lrs);  