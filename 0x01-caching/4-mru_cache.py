#!/usr/bin/env python3
""" A MRU caching system """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ A class that inherits from BaseCaching and is a MRU caching system """

    def __init__(self):
        """ class constructor """

        super().__init__()  # calling the Parent class constructor
        self.used_cache = []

    def put(self, key, item):
        """ Add an item in the cache. If number of items is higher than
            MAX_ITEMS, discard the most recently used item
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_item = self.used_cache.pop(-1)
            print(f"DISCARD: {mru_item}")
            self.cache_data.pop(mru_item)

        if key in self.cache_data:
            self.cache_data[key] = item
            self.used_cache.remove(key)
            self.used_cache.append(key)
        else:
            self.cache_data[key] = item
            self.used_cache.append(key)

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None
        else:
            if key in self.cache_data:
                self.used_cache.remove(key)
                self.used_cache.append(key)
                return self.cache_data[key]
