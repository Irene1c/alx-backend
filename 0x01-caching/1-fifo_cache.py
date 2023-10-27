#!/usr/bin/env python3
""" A FIFO caching system """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ A class that inherits from BaseCaching and is a FIFO caching system """

    def __init__(self):
        """ class constructor """

        super().__init__()  # calling the Parent class constructor
        self.cache_list = []

    def put(self, key, item):
        """ Add an item in the cache. If number of items is higher than
            MAX_ITEMS, discard the first item put in cache
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_item = self.cache_list.pop(0)
            print(f"DISCARD: {first_item}")
            self.cache_data.pop(first_item)

        self.cache_data[key] = item
        self.cache_list.append(key)

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
