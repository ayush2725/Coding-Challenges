'''
Author: Ayush Singh

Question:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Logic:
Since the array is not guaranteed to be sorted, we'll maintain a hash-set to store the values in the array, if that value exists in set, we'll
return True, else, false

Time Complexity: O(n)
Space Complexity: o(n)
'''

# Implementation to the Solutiton class
class Solution(object):
  
    def containsDuplicate(self, nums):
        
        # Initializing the hash-set
        set_of_nums = set()
        
        # Iterating through all elements and checking for duplicates
        for i in nums:
            if i in set_of_nums:
                return True
            set_of_nums.add(i)
            
        # Case when no duplicates were found
        return False
