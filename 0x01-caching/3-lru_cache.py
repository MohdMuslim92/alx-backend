#!/usr/bin/python3
""" LRUCache module
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and implements a caching system
    using LRU
    """
    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.lru_tracker = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded_key, _ = self.lru_tracker.popitem(last=False)
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            if key in self.lru_tracker:
                del self.lru_tracker[key]
            self.lru_tracker[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end to indicate it's the most
            # recently used
            value = self.cache_data[key]
            del self.lru_tracker[key]
            self.lru_tracker[key] = value
            return value
        return None
