'''
Author: Ayush Singh

Question:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Logic:
We'll be maintaining a queue. Starting from appending the root, we'll keep on appending the peek() element's left child, then right child,
this'll go left to right for each level of the binary tree

Time complexity: O(n)
Space complexity: O(n)
'''

# Definition for a binary tree node.
class TreeNode(object):
    
    def __init__(self, val=0, left=None, right=None):
        
        self.val = val
        self.left = left
        self.right = right
        
# Definition of the Solution class
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
        
        return root
