'''
Author: Ayush Singh

Question:
You are given the root of a binary search tree (BST) and an integer val.Find the node in the BST that the node's value equals val and
return the subtree rooted with that node. If such a node does not exist, return null.

Logic:
By a BST's property, we'll start at the root, if the val is greater, we go to the right sub-tree, else, we go to the left sub-tree. This'll
go on until we hit a null node

Time Complexity: O(log n)
Space Complexity: O(1)
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
# Implementation to the Solution class
class Solution(object):
    def searchBST(self, root, val):
        
        # Initializing a current node 
        curr_node = root
        
        while curr_node != None:
            
            if (curr_node.val == val):
                return curr_node
            
            elif (curr_node.val > val):
                curr_node = curr_node.left
            
            else:
                curr_node = curr_node.right
        
        return None
