# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        
        lst = []
        
        self.helper(root, lst)
        
        return lst
    
    def helper(self, Node, lst):
        
        if Node != None:
            
            self.helper(Node.left, lst)
            
            self.helper(Node.right, lst)
            
            lst.append(Node.val)
            
