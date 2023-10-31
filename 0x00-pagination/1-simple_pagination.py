#!/usr/bin/env python3
""" Pagination of a CSV file """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Function that returns a tuple containing a start and an end index
        corresponding to the range of indexes to return in a list for the
        particular pagination parameters.
    """

    if page == 1:
        return 0, page_size
    else:
        start_idx = (page - 1) * page_size
        end_idx = page * page_size
        return start_idx, end_idx


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Simple pagination """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0

        start, end = index_range(page, page_size)
        try:
            data = self.dataset()
            page_data = data[start:end]
            return page_data
        except IndexError:
            return []
