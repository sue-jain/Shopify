from typing import List
import unittest

def find(A: List[int]) -> int:
    """
    Find the index of the smallest element in a cyclically shifted array.
    
    Args:
        A (List[int]): A cyclically shifted sorted array
        
    Returns:
        int: Index of the smallest element
        
    Raises:
        ValueError: If the input array is empty
    """
    if not A:
        raise ValueError("Array cannot be empty")
    
    if len(A) == 1:
        return 0
    
    # If array is already sorted (not rotated)
    if A[0] < A[-1]:
        return 0
    
    left, right = 0, len(A) - 1
    
    while left <= right:
        # If we're down to one element
        if left == right:
            return left
            
        mid = (left + right) // 2
        
        # If mid+1 exists and mid is greater than mid+1, 
        # then mid+1 is the smallest
        if mid < len(A) - 1 and A[mid] > A[mid + 1]:
            return mid + 1
            
        # If mid exists and mid-1 is greater than mid,
        # then mid is the smallest
        if mid > 0 and A[mid - 1] > A[mid]:
            return mid
            
        # If mid is greater than left, then check right half
        if A[mid] > A[left]:
            if A[mid] > A[right]:
                left = mid + 1
            else:
                right = mid - 1
        # If mid is less than left, then check left half
        else:
            right = mid - 1
            
    return left

class TestCyclicArray(unittest.TestCase):
    """Test cases for find function"""
    
    def test_empty_array(self):
        """Test with empty array"""
        with self.assertRaises(ValueError):
            find([])
    
    def test_single_element(self):
        """Test with single element array"""
        self.assertEqual(find([1]), 0)
    
    def test_two_elements_sorted(self):
        """Test with two elements in sorted order"""
        self.assertEqual(find([1, 2]), 0)
    
    def test_two_elements_rotated(self):
        """Test with two elements rotated"""
        self.assertEqual(find([2, 1]), 1)
    
    def test_sorted_array(self):
        """Test with already sorted array"""
        self.assertEqual(find([1, 2, 3, 4, 5]), 0)
    
    def test_rotated_once(self):
        """Test with array rotated by one position"""
        self.assertEqual(find([5, 1, 2, 3, 4]), 1)
    
    def test_rotated_multiple(self):
        """Test with array rotated multiple positions"""
        self.assertEqual(find([3, 4, 5, 1, 2]), 3)
    
    def test_rotated_last(self):
        """Test with array rotated to last position"""
        self.assertEqual(find([2, 3, 4, 5, 1]), 4)
    
    def test_duplicate_elements(self):
        """Test with array containing duplicate elements"""
        self.assertEqual(find([3, 3, 4, 1, 2]), 3)
    
    def test_large_array(self):
        """Test with large array"""
        arr = list(range(1000, 2000)) + list(range(0, 1000))
        self.assertEqual(find(arr), 1000)
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(find([-2, -1, -5, -4, -3]), 2)
    
    def test_all_same_elements(self):
        """Test with all same elements"""
        self.assertEqual(find([1, 1, 1, 1, 1]), 0)

def print_test_cases():
    """Print example test cases and their results"""
    test_cases = [
        [],                     # Empty array
        [1],                    # Single element
        [1, 2],                # Sorted array
        [2, 1],                # Rotated array
        [1, 2, 3, 4, 5],       # Sorted array
        [5, 1, 2, 3, 4],       # Rotated once
        [3, 4, 5, 1, 2],       # Rotated multiple times
        [2, 3, 4, 5, 1],       # Rotated to last
        [3, 3, 4, 1, 2],       # With duplicates
        [-2, -1, -5, -4, -3],  # Negative numbers
        [1, 1, 1, 1, 1]        # All same elements
    ]
    
    print("Testing find function with various cases:")
    print("=" * 50)
    
    for arr in test_cases:
        try:
            result = find(arr)
            print(f"Array: {arr}")
            if arr:  # If array is not empty
                print(f"Smallest element {arr[result]} found at index {result}")
            print("-" * 50)
        except ValueError as e:
            print(f"Array: {arr}")
            print(f"Error: {e}")
            print("-" * 50)

if __name__ == "__main__":
    # Run example test cases
    print_test_cases()
    print("\nRunning unit tests:")
    print("=" * 50)
    unittest.main(argv=[''], exit=False, verbosity=2) 