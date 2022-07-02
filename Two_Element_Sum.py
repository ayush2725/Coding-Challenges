'''
Author: Ayush Singh

Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Logic:
By basic mathematics: if a + b = c, then, given we have a and c, b = c - a. Using the same logic, we'll be maintaining a Dictionary whose keys will
be the difference between current element and the target and whose value will be the index. Once we find an element whose key is in the dictionary,
we return those indices, else, we return an empty list

Time Complexity: O(n)
Space Complexity: O(n)
'''

# Implementation to the Solution class
class Solution(object):
    def twoSum(self, nums, target):
        
        # Dictionary to store the indices and its index
        dict_of_nums = {}
        
        # Iterating through all elements in the list
        for i in range(len(nums)):
            
            num = nums[i]
            
            # Case when the sum is found
            if num in dict_of_nums:
                return [i, dict_of_nums[num]]
            
            # Else, appending the difference to the dictionary
            else:
                dict_of_nums[target - num] = i
        
        # When no elements equal to target is found, we return an empty list
        return []
