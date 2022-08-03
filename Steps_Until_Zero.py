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
