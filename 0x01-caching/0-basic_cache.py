#!/usr/bin/python3
""" BasicCache module that implements caching without limits
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and implements a caching
        system without limits
    """
    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
