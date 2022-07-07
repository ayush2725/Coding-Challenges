# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
