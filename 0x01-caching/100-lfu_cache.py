#!/usr/bin/python3
""" LFUCache module
"""


from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and implements a caching system
    using LFU
    """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequencies = defaultdict(int)
        self.keys_by_frequency = defaultdict(list)
        self.min_frequency = 0

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequencies[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    while self.keys_by_frequency[self.min_frequency] == []:
                        self.min_frequency += 1
                    key_to_remove = (
                            self.keys_by_frequency[self.min_frequency].pop(0))
                    del self.cache_data[key_to_remove]
                    del self.frequencies[key_to_remove]

                    print(f"DISCARD: {key_to_remove}")

                self.cache_data[key] = item
                self.frequencies[key] = 1
                self.keys_by_frequency[1].append(key)
                self.min_frequency = 1

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.frequencies[key] += 1

            old_freq = self.frequencies[key] - 1
            if key in self.keys_by_frequency[old_freq]:
                self.keys_by_frequency[old_freq].remove(key)

            self.keys_by_frequency[self.frequencies[key]].append(key)

            return self.cache_data[key]
        return None
