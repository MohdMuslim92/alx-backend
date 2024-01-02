#!/usr/bin/python3
""" MRUCache module
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements a caching system
    using MRU
    """
    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.mru_tracker = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.mru_tracker.remove(key)
                else:
                    # Discard the most recently used item
                    discarded_key = self.mru_tracker.pop()
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            if key in self.mru_tracker:
                self.mru_tracker.remove(key)
            self.mru_tracker.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end to indicate it's the most
            # recently used
            self.mru_tracker.remove(key)
            self.mru_tracker.append(key)
            return self.cache_data[key]
        return None
