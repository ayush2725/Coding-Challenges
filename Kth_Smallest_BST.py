# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
