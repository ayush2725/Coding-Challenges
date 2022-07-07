'''
Author: Ayush Singh

Question:
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST. According to the definition of LCA 
on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

Logic: 
Starting at the root node, if 1st Node's value is in the left sub-tree and 2nd Node's value is in the right sub-tree, this means there is a 
split in the tree, and hence, that node will be lowest common ancestor, since they both are in different sub-trees, they'll not have an
common ancestor going any down from the current node.
'''

# Definition for a binary tree node.
class TreeNode(object):
    
    def __init__(self, x):
        
        self.val = x
        self.left = None
        self.right = None

# Definition of the Solution class
class Solution(object):
    
    def lowestCommonAncestor(self, root, p, q):
        
        curr_node = root
        
        while curr_node != None:
            
            if curr_node.val > p.val and curr_node.val > q.val:
                
                curr_node = curr_node.left
            
            elif curr_node.val < p.val and curr_node.val < q.val:
                
                curr_node = curr_node.right
            
            else:
                
                return curr_node
