class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty"""
        return self.head is None
    
    def append(self, data):
        """
        Add a node at the end of the list
        Raises TypeError if data type doesn't match existing elements
        """
        if not self.is_empty() and not isinstance(data, type(self.head.data)):
            raise TypeError("All elements must be of the same type")
            
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def delete_node(self, node):
        """Delete the given node from the list"""
        if not node:
            return
            
        # Update size
        self.size -= 1
        
        # If node is head
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
            return
            
        # If node is tail
        if node == self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            return
            
        # If node is in middle
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def remove_duplicates(self):
        """Remove duplicate nodes from the list"""
        if self.is_empty() or self.size == 1:
            return
            
        seen = set()
        current = self.head
        
        while current:
            if current.data in seen:
                next_node = current.next
                self.delete_node(current)
                current = next_node
            else:
                seen.add(current.data)
                current = current.next
    
    def to_list(self):
        """Convert linked list to Python list for testing"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

# Unit Tests
import unittest

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()
    
    def test_empty_list(self):
        """Test removing duplicates from empty list"""
        self.dll.remove_duplicates()
        self.assertEqual(self.dll.to_list(), [])
    
    def test_single_element(self):
        """Test removing duplicates from single element list"""
        self.dll.append(1)
        self.dll.remove_duplicates()
        self.assertEqual(self.dll.to_list(), [1])
    
    def test_no_duplicates(self):
        """Test list with no duplicates"""
        values = [1, 2, 3, 4, 5]
        for val in values:
            self.dll.append(val)
        self.dll.remove_duplicates()
        self.assertEqual(self.dll.to_list(), values)
    
    def test_all_duplicates(self):
        """Test list with all duplicate elements"""
        for _ in range(5):
            self.dll.append(1)
        self.dll.remove_duplicates()
        self.assertEqual(self.dll.to_list(), [1])
    
    def test_some_duplicates(self):
        """Test list with some duplicate elements"""
        values = [1, 2, 2, 3, 3, 3, 4, 5, 5]
        for val in values:
            self.dll.append(val)
        self.dll.remove_duplicates()
        self.assertEqual(self.dll.to_list(), [1, 2, 3, 4, 5])
    
    def test_large_list(self):
        """Test large list with duplicates"""
        # Create list with numbers 0-99, repeated 3 times
        values = list(range(100)) * 3
        for val in values:
            self.dll.append(val)
        self.dll.remove_duplicates()
        self.assertEqual(self.dll.to_list(), list(range(100)))
    
    def test_negative_numbers(self):
        """Test list with negative numbers"""
        values = [-3, -2, -2, -1, 0, 0, 1, 1, 1]
        for val in values:
            self.dll.append(val)
        self.dll.remove_duplicates()
        self.assertEqual(self.dll.to_list(), [-3, -2, -1, 0, 1])
    
    def test_mixed_types(self):
        """Test list with mixed types (should raise TypeError)"""
        values = [1, "2", 3, "3", 4]
        with self.assertRaises(TypeError):
            for val in values:
                self.dll.append(val)
            self.dll.remove_duplicates()

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False, verbosity=2)

"""
Time Complexity: O(n) where n is the number of nodes
- Single traversal of the list
- Hash table lookups are O(1)

Space Complexity: O(n)
- Uses a hash set to store unique values
- In worst case, all elements are unique

Trade-offs:
- Chose hash table approach for O(n) time complexity
- Alternative would be O(n²) time with O(1) space using nested loops
- Current approach is more efficient for large lists
""" 