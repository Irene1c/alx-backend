#!/usr/bin/env python3
"""  Simple helper function """
from typing import Tuple


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
