
import math

class Node:
    """
    A node in a binary tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst_satisfied(node, min_val=float('-inf'), max_val=float('inf')):
    """
    Determines if a binary tree satisfies the Binary Search Tree (BST) property.

    The BST property states that:
    - Every node in the left subtree has a value smaller than the current node.
    - Every node in the right subtree has a value larger than the current node.
    - Both the left and right subtrees must also be valid BSTs.

    Args:
        node (Node): The current node being checked (starts with the root).
        min_val (float): The minimum allowed value for the current node.
        max_val (float): The maximum allowed value for the current node.

    Returns:
        bool: True if the tree satisfies the BST property, False otherwise.
    """
    # Base case: An empty tree is a valid BST
    if node is None:
        return True

    # Check if the current node's value is within the allowed range
    # Using strict inequality as per the problem statement (smaller/larger than)
    if not (min_val < node.value < max_val):
        return False

    # Recursively check the left and right subtrees
    # For the left subtree, the max_val becomes the current node's value
    # For the right subtree, the min_val becomes the current node's value
    return (is_bst_satisfied(node.left, min_val, node.value) and
            is_bst_satisfied(node.right, node.value, max_val))
