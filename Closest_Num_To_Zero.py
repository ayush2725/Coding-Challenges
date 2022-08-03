'''
Author: Ayush Singh

Question:
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, 
return the number with the largest value.

Logic:
Starting from the 0th index of the array, we'll iterate through all the elements in the array and will see whose abs() value is closest to
zero. We'll also keep a condition to make sure if there are duplicates, we return only the positive part.

Time Complexity: O(n)
Space Complexity: o(1)
'''

class Solution(object):
    def findClosestNumber(self, nums):
        
        closest_num = float('inf')
        closest_sum = float('inf')
        
        for i in nums:
            
            if abs(i) < closest_sum:
                closest_sum = abs(i)
                closest_num = i
            
            elif abs(i) == closest_sum and i > 0:
                closest_num = i
                
        return closest_num
