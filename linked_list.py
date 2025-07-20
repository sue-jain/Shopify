
class Node:
    """
    A node in a singly linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a singly linked list.

    Args:
        head: The head of the linked list.

    Returns:
        The new head of the reversed linked list.
    """
    # Initialize three pointers: prev, current, and next.
    # prev points to the previous node, initialized to None.
    # current points to the current node, initialized to the head.
    # next is used to store the next node in the original list.
    prev = None
    current = head
    next = None

    # Iterate through the linked list.
    while current is not None:
        # Store the next node.
        next = current.next
        # Reverse the pointer of the current node to point to the previous node.
        current.next = prev
        # Move the prev and current pointers one step forward.
        prev = current
        current = next

    # After the loop, prev will be pointing to the new head of the reversed list.
    head = prev
    return head

def print_linked_list(head):
    """
    Prints the linked list.
    """
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def is_balanced_parentheses(s):
    """
    Checks if the parentheses in the string are balanced.
    Supports (), {}, and [].
    Args:
        s (str): The input string.
    Returns:
        bool: True if balanced, False otherwise.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack

# Example usage:
if __name__ == '__main__':
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

    print("Original linked list:")
    print_linked_list(head)

    # Reverse the linked list.
    reversed_head = reverse_linked_list(head)

    print("\nReversed linked list:")
    print_linked_list(reversed_head)

    print("\nTesting is_balanced_parentheses:")
    test_cases = [
        ("()", True),
        ("([])", True),
        ("([)]", False),
        ("((()))", True),
        ("((())", False),
        ("", True),
        ("{[()]}[]", True),
        ("{[(])}", False),
        ("([{}])", True),
        ("([{})]", False),
    ]
    for expr, expected in test_cases:
        result = is_balanced_parentheses(expr)
        print(f"is_balanced_parentheses('{expr}') = {result} (Expected: {expected})")
