'''
Author: Ayush Singh

Question:
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Logic:
We'll perform an in-order transversal of the tree. This'll return us an array in the increasing order. Starting from 0th index, we'll go to 
(k-1)th index, that will be the kth smallest element.

Time Complexity: O(n)
Space Complexity: O(d)    d is the depth of the tree
'''

# Definition for a binary tree node.
class TreeNode(object):
    
    def __init__(self, val=0, left=None, right=None):
        
        self.val = val
        self.left = left
        self.right = right
        
# Definition of the Solution class
class Solution(object):
    def kthSmallest(self, root, k):
        
        lst = []
        
        self.helper(root, lst)
        
        return lst[k - 1]
        
    def helper(self, Node, lst):
        
        if Node != None:
            
            self.helper(Node.left, lst)
            lst.append(Node.val)
            self.helper(Node.right, lst)
