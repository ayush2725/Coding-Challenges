'''
Author: Ayush Singh

Question:
Given an integer num, return the number of steps to reduce it to zero.In one step, if the current number is even, you have to divide 
it by 2, otherwise, you have to subtract 1 from it.

Logic:
Using a while, the condition would be for the number to always be positive, then, we'll see if the number is even or odd and do the 
appropriate operation keeping a track of the number of operations, and once the condition is false, we'll return the number of
operations.

Time Complexity: O(1)
Space Complexity: o(1)
'''

class Solution(object):
    def numberOfSteps(self, num):
        
        no_of_steps = 0
        
        while num > 0:
            
            no_of_steps += 1
            
            if num % 2 == 0:
                num /= 2
            
            else:
                num -= 1
        
        return no_of_steps
