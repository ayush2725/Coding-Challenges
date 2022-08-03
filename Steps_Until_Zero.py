'''
Author: Ayush Singh

Question:
You are given two non-negative integers num1 and num2. In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise 
subtract num1 from num2. Return the number of operations required to make either num1 = 0 or num2 = 0.

Logic:
Using a while loop, the condition would be for both the numbers to be positive, inside the loop, we'll see if either of the numbers is 
zero, if it is, we break out of the loop, else, we substract the numbers.

Time Complexity: O(n)
Space Complexity: o(1)
'''

class Solution(object):
    def countOperations(self, num1, num2):
        
        no_of_steps = 0
        
        while num1 > 0 and num2 > 0:
            
            if num1 == 0 or num2 == 0:
                break
            
            elif num1 > num2:
                num1 = num1 - num2
                no_of_steps += 1
            
            else:
                num2 = num2 - num1
                no_of_steps += 1
        
        return no_of_steps
