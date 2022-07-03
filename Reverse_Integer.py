'''
Author: Ayush Singh

Question:
Given a signed integer x, return x with its digits reversed.

Logic:
Since integers are signed, we'll be maintaining keeping a variable to store their sign and will take its absolute value. 
num % 10 will give the last digit and num / 10 will remove the last digit
'''

# Implementation to the Solution class
class Solution(object):
  
    def reverse(self, x):
        
        # Storing the sign of the number
        if x >= 0:
            sign = 1
        else:
            sign = -1
        
        # Taking the number's abs value
        x = abs(x)
        
        # Variable to store the reversed number
        rev_num = 0
        
        # Reversing the number
        while x != 0:
            
            rev_num = (rev_num * 10) + (x % 10)
            x = x / 10
        
        return sign*rev_num
