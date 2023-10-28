#!/usr/bin/env python3
""" A LFU caching system """
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ A class that inherits from BaseCaching and is a LFU caching system """

    def __init__(self):
        """ class constructor """

        super().__init__()  # calling the Parent class constructor
        self.freq_cache = {}

    def put(self, key, item):
        """ Add an item in the cache. If number of items is higher than
            MAX_ITEMS, discard the least frequently used item
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_item = min(self.freq_cache, key=self.freq_cache.get)
            self.freq_cache.pop(lfu_item)
            print(f"DISCARD: {lfu_item}")
            self.cache_data.pop(lfu_item)

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq_cache[key] += 1
        else:
            self.cache_data[key] = item
            self.freq_cache[key] = 1

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None
        else:
            if key in self.cache_data:
                self.freq_cache[key] += 1
                return self.cache_data[key]
