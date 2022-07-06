'''
Author: Ayush Singh

Question:
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after 
the insertion. It is guaranteed that the new value does not exist in the original BST.Notice that there may exist multiple valid ways
for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Logic:
We'll start from the root, if the value is greater than the node's value, we go to the right child, else, we go the left child. Inside each
transition, we'll check if the child is None, since that will be the position to insert. The only corner case is when the tree is empty,
in which case the root will be the Node.

Time Complexity: O(log n)
Space Complexity: O(1)
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    
    def insertIntoBST(self, root, val):
        
        if root == None:
            root = TreeNode(val)
        
        else:
            curr_node = root

            while curr_node != None:

                if val > curr_node.val:

                    if curr_node.right == None:

                        curr_node.right = TreeNode(val)
                        break

                    else:    
                        curr_node = curr_node.right

                else:
                    if curr_node.left == None:
                        curr_node.left = TreeNode(val)
                        break

                    else:
                        curr_node = curr_node.left
                
        return
