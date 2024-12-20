#!/usr/bin/env python3
"""The Basic dictionary module"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines:
    Basic dictionary"""

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
