Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

Example:

Input:
x = 10
Output:
1 4 9
Explanation:
From 1 to 10, numbers in powers
of 2 are, 12, 22, 32 as 1, 4 and 9.
Your Task:
This is a function problem. You need to complete the function printIncreasingPower().

Constraints:
2 <= x <= 103

Solution:

def printIncreasingPower(x):
    ##Your code here
    i=1
    # Loop to jump in powers of 2
    while(i**2<=x):
        ##Your code here
        
        print (i**2 , end = " ")
        i+=1
     
