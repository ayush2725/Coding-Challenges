'''
Author: Ayush Singh

Question:
Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:
1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

Logic:
We'll be solving this question with recursion. The condition will be the node's value should be strictly less that min_val and strictly greater
than the max_val. we'll be recursively calling this function on the left sub-tree and then the right sub-tree and will be checking this condition.

Time complexity: O(n)
Space complexity: O(d)    d: depth of the tree
'''

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# Implementation to the Solution class
class Solution(object):
    def isValidBST(self, root):
        
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, Node, min_val, max_val):
        
        if Node == None:
            return True
        
        if Node.val <= min_val or Node.val >= max_val:
            return False
        
        left_sub_tree = self.helper(Node.left, min_val, Node.val)
        right_sub_tree = self.helper(Node.right, Node.val, max_val)
        
        return left_sub_tree and right_sub_tre
        
