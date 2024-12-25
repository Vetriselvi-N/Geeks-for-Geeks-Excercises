You are given a string str, you need to print its characters at even indices(index starts at 0).

Note: Please go through the range function to understand how to jump 2 steps.

Example 1:

Input:
str = DoctorPhenomenal
Output:
DcoPeoea
Example 2:

Input:
str = Geeks
Output:
Ges
Your Task:
This is a function problem. You don't need to take input. Just complete the function stringJumper() that takes str as input.

Solution:

def stringJumper(str):
    for i in range(0,len(str),2): 
        print(str[i], end="") 
