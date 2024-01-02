#!/usr/bin/python3
""" LIFOCache module
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and implements a caching system
    using LIFO
    """
    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.queue.remove(key)
                else:
                    discarded_key = self.queue.pop() if self.queue else None
                    if discarded_key:
                        del self.cache_data[discarded_key]
                        print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
