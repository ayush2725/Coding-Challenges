'''
Author: Ayush Singh

Question:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Logic:
We'll recursively reach the end of the left sub-tree, print it going to top, then recursively call the function on the right sub-tree

Time Complexity: O(n)
Space Complexity: O(d)  d: depth of the tree
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
# Implementation to the Solution class
class Solution(object):
    
    def inorderTraversal(self, root):
        
        lst = []
        self.helper(root, lst)
        
        return lst
    
    def helper(self, Node, lst):
        
        if Node != None:
            
            self.helper(Node.left, lst)
            
            lst.append(Node.val)
            
            self.helper(Node.right, lst)
