import pytest
from bst_checker import Node, is_bst_satisfied

# Helper function to build a tree from a list (for convenience in tests)
def build_tree(nodes):
    if not nodes:
        return None
    root = Node(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = Node(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = Node(nodes[i])
            queue.append(current.right)
        i += 1
    return root

# Test cases for valid BSTs
def test_valid_bsts():
    # Empty tree
    assert is_bst_satisfied(None) == True

    # Single node tree
    assert is_bst_satisfied(Node(5)) == True

    # Simple valid BST
    #     5
    #    / \
    #   3   8
    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(8)
    assert is_bst_satisfied(root1) == True

    # More complex valid BST
    #       10
    #      /  \
    #     5    15
    #    / \  /  \
    #   3   7 12  18
    root2 = Node(10)
    root2.left = Node(5)
    root2.right = Node(15)
    root2.left.left = Node(3)
    root2.left.right = Node(7)
    root2.right.left = Node(12)
    root2.right.right = Node(18)
    assert is_bst_satisfied(root2) == True

    # Left-skewed tree (still valid BST)
    #   5
    #  /
    # 4
    # /
    # 3
    root3 = Node(5)
    root3.left = Node(4)
    root3.left.left = Node(3)
    assert is_bst_satisfied(root3) == True

    # Right-skewed tree (still valid BST)
    # 5
    #  \
    #   6
    #    \
    #     7
    root4 = Node(5)
    root4.right = Node(6)
    root4.right.right = Node(7)
    assert is_bst_satisfied(root4) == True

# Test cases for invalid BSTs
def test_invalid_bsts():
    # Left child greater than root
    #     5
    #    / \
    #   7   8
    root1 = Node(5)
    root1.left = Node(7)
    root1.right = Node(8)
    assert is_bst_satisfied(root1) == False

    # Right child smaller than root
    #     5
    #    / \
    #   3   2
    root2 = Node(5)
    root2.left = Node(3)
    root2.right = Node(2)
    assert is_bst_satisfied(root2) == False

    # Duplicate value (violates strict inequality)
    #     5
    #    / \
    #   5   8
    root3 = Node(5)
    root3.left = Node(5)
    root3.right = Node(8)
    assert is_bst_satisfied(root3) == False

    # Duplicate value (violates strict inequality)
    #     5
    #    / \
    #   3   5
    root4 = Node(5)
    root4.left = Node(3)
    root4.right = Node(5)
    assert is_bst_satisfied(root4) == False

    # Subtree violation (right child of left subtree is too large)
    #       10
    #      /  \
    #     5    15
    #      \
    #       12  <-- This 12 is in the left subtree of 10, but is > 10
    root5 = Node(10)
    root5.left = Node(5)
    root5.right = Node(15)
    root5.left.right = Node(12)
    assert is_bst_satisfied(root5) == False

    # Subtree violation (left child of right subtree is too small)
    #       10
    #      /  \
    #     5    15
    #         /
    #        7  <-- This 7 is in the right subtree of 10, but is < 10
    root6 = Node(10)
    root6.left = Node(5)
    root6.right = Node(15)
    root6.right.left = Node(7)
    assert is_bst_satisfied(root6) == False

    # Complex invalid tree
    #       20
    #      /  \
    #     10   30
    #    /  \  /  \
    #   5   25 25  35  <-- 25 in left subtree of 20, but > 20
    root7 = Node(20)
    root7.left = Node(10)
    root7.right = Node(30)
    root7.left.left = Node(5)
    root7.left.right = Node(25) # INVALID: 25 > 20
    root7.right.left = Node(25)
    root7.right.right = Node(35)
    assert is_bst_satisfied(root7) == False
