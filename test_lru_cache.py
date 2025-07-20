
import unittest
from lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):

    def test_cache_initialization(self):
        """Test that the cache is initialized correctly."""
        cache = LRUCache(2)
        self.assertEqual(cache.capacity, 2)
        self.assertEqual(len(cache.cache), 0)

    def test_put_and_get(self):
        """Test the basic put and get functionality."""
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

    def test_lru_eviction(self):
        """Test that the least recently used item is evicted."""
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)  # This should evict key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 2)
        self.assertEqual(cache.get(3), 3)

    def test_get_updates_recency(self):
        """Test that getting an item updates its recency."""
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)  # Access key 1, making it the most recently used
        cache.put(3, 3)  # This should evict key 2
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(3), 3)

    def test_put_updates_existing_key(self):
        """Test that putting an existing key updates its value."""
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)

if __name__ == '__main__':
    unittest.main()
