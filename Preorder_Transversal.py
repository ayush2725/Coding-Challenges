'''
Author: Ayush Singh

Question:
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Logic:
Preorder transversal is Node, Node.left, and Node.right. So, we'll be recursively calling it and adding the node, then calling it
on Node.left, then Node.right

Time Complexity: 
Space Complexity:
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution(object):
    def preorderTraversal(self, root):
        
        lst = []
        
        self.helper(root, lst)
        
        return lst
    
    def helper(self, Node, lst):
        
        if Node != None:
            
            lst.append(Node.val)

            self.helper(Node.left, lst)

            self.helper(Node.right, lst)
