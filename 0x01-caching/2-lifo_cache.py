#!/usr/bin/env python3
""" A LIFO caching system """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ A class that inherits from BaseCaching and is a LIFO caching system """

    def __init__(self):
        """ class constructor """

        super().__init__()  # calling the Parent class constructor

    def put(self, key, item):
        """ Add an item in the cache. If number of items is higher than
            MAX_ITEMS, discard the last item put in cache
        """

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = self.cache_data.popitem()
            print(f"DISCARD: {last_item[0]}")

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """

        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
