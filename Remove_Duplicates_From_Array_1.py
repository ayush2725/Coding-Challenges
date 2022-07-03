'''
Author: Ayush Singh

Question:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Return the length of the array.
[1,2,2] -> [1,2]

Logic:
Keeping 2 pointers, we'll compare if the values at the two indices are same, if they are, we remove the 2nd pointer's index, else,
we increment both the pointers

Time Complexity: O(n)
Space Complexity: O(1)
'''

# Implementation to the Solution class
class Solution(object):
    def removeDuplicates(self, nums):
        
        # Two pointers, slow and fast 
        slow = 0
        fast = 1
        
        while fast < len(nums):
            
            # Case when there are duplicates
            if nums[slow] == nums[fast]:
                
                del nums[fast]
            
            # Case when there aren't duplicates
            else:
                slow += 1
                fast += 1
        
        return len(nums)        
