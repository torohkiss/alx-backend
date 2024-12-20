#!/usr/bin/env python3
"""The FIFOCache module"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """The FIFOCache that uses the FIFO algorithm"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adding items to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = next(iter(self.cache_data))
            self.cache_data.pop(first_item)
            print(f"DISCARD: {first_item}")

    def get(self, key):
        """Retrieves items from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
