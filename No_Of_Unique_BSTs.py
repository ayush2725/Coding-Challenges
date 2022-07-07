'''
Author: Ayush Singh

Question:
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Logic:
We know that the values will be in increasing order. For example: Let the values be [1,2,3]. Taking 1 as the root, we will have no values
in the left-subtree and 2 different combinations in right. Taking 2 as the root, we'll have exactly one value in left subtree and one in right.
Taking 3 as the root, there'll be 0 values in the right sub-tree and 2 combinations in the left sub-tree. So, its C0C2, C1C1, C2C0. Following 
this pattern, it's the catalan number. That sums up to [(2n)C(n)]/(n+1)

Time Complexity: O(1)
Space Complexity: O(1)
'''

import math

class Solution(object):
    
    
    def nCr(self, n,r):
        
        f = math.factorial
        
        return f(n) // f(r) // f(n-r)
    
    def numTrees(self, n):
        
        num = self.nCr(2*n, n)
        
        return num // (n+1)
