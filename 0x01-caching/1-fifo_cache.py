#!/usr/bin/python3
""" FIFOCache module
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and implements a caching system
    using FIFO
    """
    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.queue:
                    discarded_key = self.queue.pop(0)
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")
            else:
                self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
