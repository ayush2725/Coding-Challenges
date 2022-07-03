'''
Author: Ayush Singh

Question:
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.In Pascal's triangle, each number is the sum of the
two numbers directly above it. Example: If input is 3, return [1,2,1], since pascal's triangle until 3rd row is [[1], [1, 1], [1, 2, 1]]

Logic:
Analyzing closely, elements of a row is given by the formula nCr, where n is number of row and r is the number of the column. Both of them
indexed at zero. No. of columns = no. of rows + 1
'''

import math

# Implementation to the Solution class
class Solution(object):
    
    # Helper method to calculate nCr
    def nCr(self, n,r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)
    
    # Main method
    def getRow(self, rowIndex):
        
        lst = []
        
        for i in range(rowIndex + 1):
            
            lst.append(self.nCr(rowIndex, i))
        
        return lst    
