import json
from typing import List, Dict, Any, Callable, Optional
from collections import defaultdict
import unittest

def deduplicate_by_key(objects: List[Dict], key: str) -> List[Dict]:
    """
    Deduplicate objects based on a specific key.
    Keeps the first occurrence of each unique key value.
    
    Args:
        objects: List of dictionaries to deduplicate
        key: The key to use for deduplication
    
    Returns:
        List of deduplicated objects
    """
    seen = set()
    result = []
    
    for obj in objects:
        if key not in obj:
            continue
        if obj[key] not in seen:
            seen.add(obj[key])
            result.append(obj)
    
    return result

def deduplicate_by_multiple_keys(objects: List[Dict], keys: List[str]) -> List[Dict]:
    """
    Deduplicate objects based on multiple keys.
    Keeps the first occurrence of each unique combination of key values.
    
    Args:
        objects: List of dictionaries to deduplicate
        keys: List of keys to use for deduplication
    
    Returns:
        List of deduplicated objects
    """
    seen = set()
    result = []
    
    for obj in objects:
        # Create a tuple of values for the specified keys
        key_values = tuple(obj.get(key) for key in keys)
        if key_values not in seen:
            seen.add(key_values)
            result.append(obj)
    
    return result

def deduplicate_by_custom_function(objects: List[Dict], key_func: Callable[[Dict], Any]) -> List[Dict]:
    """
    Deduplicate objects using a custom function to generate the key.
    
    Args:
        objects: List of dictionaries to deduplicate
        key_func: Function that takes an object and returns a key for deduplication
    
    Returns:
        List of deduplicated objects
    """
    seen = set()
    result = []
    
    for obj in objects:
        key = key_func(obj)
        if key not in seen:
            seen.add(key)
            result.append(obj)
    
    return result

def deduplicate_by_json_string(objects: List[Dict]) -> List[Dict]:
    """
    Deduplicate objects by converting them to JSON strings.
    This removes objects with identical content regardless of key order.
    
    Args:
        objects: List of dictionaries to deduplicate
    
    Returns:
        List of deduplicated objects
    """
    seen = set()
    result = []
    
    for obj in objects:
        # Sort keys to ensure consistent JSON representation
        json_str = json.dumps(obj, sort_keys=True)
        if json_str not in seen:
            seen.add(json_str)
            result.append(obj)
    
    return result

def deduplicate_keep_latest(objects: List[Dict], key: str, timestamp_key: str = 'timestamp') -> List[Dict]:
    """
    Deduplicate objects based on a key, keeping the latest version based on timestamp.
    
    Args:
        objects: List of dictionaries to deduplicate
        key: The key to use for deduplication
        timestamp_key: The key containing timestamp information
    
    Returns:
        List of deduplicated objects with latest timestamps
    """
    latest_objects = {}
    
    for obj in objects:
        if key not in obj:
            continue
            
        obj_key = obj[key]
        current_timestamp = obj.get(timestamp_key, 0)
        
        if obj_key not in latest_objects or current_timestamp > latest_objects[obj_key].get(timestamp_key, 0):
            latest_objects[obj_key] = obj
    
    return list(latest_objects.values())

# Test cases
def run_test_cases():
    """Run comprehensive test cases for all deduplication functions."""
    
    print("🧪 Running Deduplication Test Cases")
    print("=" * 60)
    
    # Test data
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 30},
        {"id": 1, "name": "Alice Updated", "email": "alice@example.com", "age": 26},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 35},
        {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 30},
    ]
    
    products = [
        {"id": "p1", "name": "Laptop", "category": "Electronics", "price": 999},
        {"id": "p2", "name": "Phone", "category": "Electronics", "price": 599},
        {"id": "p1", "name": "Laptop Pro", "category": "Electronics", "price": 1299},
        {"id": "p3", "name": "Book", "category": "Books", "price": 19},
    ]
    
    orders = [
        {"order_id": "o1", "user_id": 1, "amount": 100, "timestamp": 1000},
        {"order_id": "o2", "user_id": 2, "amount": 200, "timestamp": 1100},
        {"order_id": "o3", "user_id": 1, "amount": 150, "timestamp": 1200},
        {"order_id": "o4", "user_id": 3, "amount": 300, "timestamp": 1300},
    ]
    
    # Test 1: Deduplicate by single key
    print("\n📋 Test 1: Deduplicate by single key (id)")
    print("-" * 40)
    original_count = len(users)
    deduplicated = deduplicate_by_key(users, "id")
    print(f"Original count: {original_count}")
    print(f"Deduplicated count: {len(deduplicated)}")
    print("Deduplicated users:")
    for user in deduplicated:
        print(f"  - ID: {user['id']}, Name: {user['name']}")
    
    # Test 2: Deduplicate by multiple keys
    print("\n📋 Test 2: Deduplicate by multiple keys (name, email)")
    print("-" * 40)
    deduplicated_multi = deduplicate_by_multiple_keys(users, ["name", "email"])
    print(f"Original count: {len(users)}")
    print(f"Deduplicated count: {len(deduplicated_multi)}")
    print("Deduplicated users:")
    for user in deduplicated_multi:
        print(f"  - Name: {user['name']}, Email: {user['email']}")
    
    # Test 3: Deduplicate by custom function
    print("\n📋 Test 3: Deduplicate by custom function (name + age)")
    print("-" * 40)
    def name_age_key(obj):
        return f"{obj['name']}_{obj['age']}"
    
    deduplicated_custom = deduplicate_by_custom_function(users, name_age_key)
    print(f"Original count: {len(users)}")
    print(f"Deduplicated count: {len(deduplicated_custom)}")
    print("Deduplicated users:")
    for user in deduplicated_custom:
        print(f"  - Name: {user['name']}, Age: {user['age']}")
    
    # Test 4: Deduplicate by JSON string
    print("\n📋 Test 4: Deduplicate by JSON string (exact content match)")
    print("-" * 40)
    duplicate_objects = [
        {"a": 1, "b": 2, "c": 3},
        {"b": 2, "a": 1, "c": 3},  # Same content, different key order
        {"a": 1, "b": 2, "c": 4},  # Different content
        {"x": 1, "y": 2},          # Different structure
    ]
    
    deduplicated_json = deduplicate_by_json_string(duplicate_objects)
    print(f"Original count: {len(duplicate_objects)}")
    print(f"Deduplicated count: {len(deduplicated_json)}")
    print("Deduplicated objects:")
    for obj in deduplicated_json:
        print(f"  - {obj}")
    
    # Test 5: Deduplicate keeping latest
    print("\n📋 Test 5: Deduplicate keeping latest by timestamp")
    print("-" * 40)
    deduplicated_latest = deduplicate_keep_latest(orders, "user_id", "timestamp")
    print(f"Original count: {len(orders)}")
    print(f"Deduplicated count: {len(deduplicated_latest)}")
    print("Latest orders per user:")
    for order in deduplicated_latest:
        print(f"  - User ID: {order['user_id']}, Amount: {order['amount']}, Timestamp: {order['timestamp']}")

# Unit Tests
class TestDeduplication(unittest.TestCase):
    """Unit tests for deduplication functions."""
    
    def setUp(self):
        """Set up test data."""
        self.users = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
            {"id": 1, "name": "Alice Updated", "email": "alice@example.com"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
        ]
    
    def test_deduplicate_by_key(self):
        """Test deduplication by single key."""
        result = deduplicate_by_key(self.users, "id")
        self.assertEqual(len(result), 3)
        ids = [user["id"] for user in result]
        self.assertEqual(set(ids), {1, 2, 3})
    
    def test_deduplicate_by_multiple_keys(self):
        """Test deduplication by multiple keys."""
        result = deduplicate_by_multiple_keys(self.users, ["name", "email"])
        self.assertEqual(len(result), 4)  # Should be 4 since Alice and Alice Updated have different names
    
    def test_deduplicate_by_custom_function(self):
        """Test deduplication by custom function."""
        def email_key(obj):
            return obj["email"]
        
        result = deduplicate_by_custom_function(self.users, email_key)
        self.assertEqual(len(result), 3)
    
    def test_deduplicate_by_json_string(self):
        """Test deduplication by JSON string."""
        objects = [
            {"a": 1, "b": 2},
            {"b": 2, "a": 1},  # Same content, different order
            {"a": 1, "b": 3},  # Different content
        ]
        result = deduplicate_by_json_string(objects)
        self.assertEqual(len(result), 2)
    
    def test_deduplicate_keep_latest(self):
        """Test deduplication keeping latest."""
        orders = [
            {"user_id": 1, "amount": 100, "timestamp": 1000},
            {"user_id": 1, "amount": 200, "timestamp": 2000},
            {"user_id": 2, "amount": 300, "timestamp": 1500},
        ]
        result = deduplicate_keep_latest(orders, "user_id", "timestamp")
        self.assertEqual(len(result), 2)
        
        # Check that we kept the latest timestamp for user_id 1
        user1_order = next(order for order in result if order["user_id"] == 1)
        self.assertEqual(user1_order["timestamp"], 2000)

if __name__ == "__main__":
    # Run test cases
    run_test_cases()
    
    print("\n" + "=" * 60)
    print("🧪 Running Unit Tests")
    print("=" * 60)
    
    # Run unit tests
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    print("\n" + "=" * 60)
    print("✅ All tests completed!")
    print("\nKey Features:")
    print("- Deduplicate by single key")
    print("- Deduplicate by multiple keys")
    print("- Deduplicate by custom function")
    print("- Deduplicate by exact content match")
    print("- Deduplicate keeping latest version") 