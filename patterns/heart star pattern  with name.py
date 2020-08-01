'''
Pattern
Heart star with name:
Enter number of rows: 10
Enter Message here: Name
    *         * 
   * *       * * 
  * * *     * * * 
 * * * *   * * * * 
* * * * * * * * * * 
* * * N a m e * * *
* * * * * * * * * * 
 * * * * * * * * * 
  * * * * * * * * 
   * * * * * * * 
    * * * * * * 
     * * * * * 
      * * * * 
       * * * 
        * * 
         * 
'''
number_rows=int(input('Enter number of rows: '))
n=number_rows//2
msg=input('Enter your message here: ')
for row in range(n):
	print(' '*(n-row-1)+'* '*(row+1),end="")
	if number_rows%2==0:
		for column in range(2*(n-row-1)):
			print(' ',end='')
	else:
		for column in range(2*(n-row-1)+1):
			print(' ',end='')
	for column in range(row+1):
			print('* ',end='')
	print()
print('* '*((number_rows-len(msg))//2)+" ".join(msg)+" *"*((number_rows-len(msg)+1)//2))
for row in range(number_rows,0,-1):
	print(' '*(number_rows-row)+'* '*(row))