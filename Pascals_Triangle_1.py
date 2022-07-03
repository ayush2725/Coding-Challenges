'''
Author: Ayush Singh

Question:
Given an integer numRows, return the first numRows of Pascal's triangle.In Pascal's triangle, each number is the sum of the two numbers directly above
Example, [[1], [1,1], [1,2,1], [1,3,3,1]]...

Logic:
If you analyze the numbers, the result is nCr where n is the number row and r is the column number, both of them start from 0-index.

Time Complexity: O(n^2)
Space Complexity: O(n)
'''

import math

# Implementation to the Solution class
class Solution(object):
    
    #Helper method to calculate nCr
    def nCr(self, n,r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)
    
    # Main method
    def generate(self, numRows):
        
        pascals_triangle = []
        
        for i in range(numRows):
            
            lst = []
            
            for j in range(i + 1):
                
                lst.append(self.nCr(i, j))
            
            pascals_triangle.append(lst)
        
        return pascals_triangle
