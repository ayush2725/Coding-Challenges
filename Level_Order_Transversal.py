# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def levelOrder(self, root):
        
        if root == None:
            return []
        
        lst = [root]
        
        l = []
        
        while len(lst) != 0:
            
            l.append(lst[0].val)
            
            if lst[0].left != None:
                lst.append(lst[0].left)
            
            if lst[0].right != None:
                lst.append(lst[0].right)
            
            del lst[0]
