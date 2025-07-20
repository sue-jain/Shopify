
from collections import OrderedDict

class LRUCache:
    """
    A simple implementation of a Least Recently Used (LRU) cache.
    """
    def __init__(self, capacity: int):
        """
        Initializes the LRU cache with a given capacity.

        Args:
            capacity: The maximum number of items the cache can hold.
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Retrieves an item from the cache.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value of the item, or -1 if the key is not in the cache.
        """
        if key not in self.cache:
            return -1
        else:
            # Move the accessed item to the end to mark it as recently used.
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Adds an item to the cache.

        If the key already exists, its value is updated. If the cache is full,
        the least recently used item is removed.

        Args:
            key: The key of the item to add.
            value: The value of the item to add.
        """
        self.cache[key] = value
        # Move the accessed item to the end to mark it as recently used.
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            # Remove the first item in the dictionary, which is the least recently used.
            self.cache.popitem(last=False)
