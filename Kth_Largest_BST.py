# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    order_array = inorder_transversal(tree, [])
	return order_array[len(order_array) - k]
	
def inorder_transversal(tree, array):
	if tree:
		inorder_transversal(tree.left, array)
		array.append(tree.value)
		inorder_transversal(tree.right, array)
	return array
