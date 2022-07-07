'''
Author: Ayush Singh

Question:
Given the root of a BST, return the Kth largest element in BST.

Logic:
We'll be in-order transversing the tree, this'll return us an array in increasing order. Once we have the array, the element at index (len - k) will be
the Kth largest element. We'll return that element.

Time Complexity: O(n)
Space Complexity: O(n)
'''

# Definition of the BST Node
class BST:
	
    def __init__(self, value, left=None, right=None):
	
        self.value = value
        self.left = left
        self.right = right

# Definition of the main method
def findKthLargestValueInBst(tree, k):
    order_array = inorder_transversal(tree, [])
	return order_array[len(order_array) - k]

# A helper method for in-order transversal
def inorder_transversal(tree, array):
	if tree:
		inorder_transversal(tree.left, array)
		array.append(tree.value)
		inorder_transversal(tree.right, array)
	return array
