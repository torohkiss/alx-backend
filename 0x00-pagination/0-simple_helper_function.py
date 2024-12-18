#!/usr/bin/env python3
"""A module that has a Simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns tuple of size two containing startindex and endindex"""

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
