#!/usr/bin/env python3
"""A module that implements a Simple pagination"""


import csv
import math
from typing import List, Dict, Any
index_range = __import__('0-simple_helper_function').index_range


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
        """gets the page needed"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        total_pages = math.ceil(len(data) / page_size)
        if page > total_pages:
            return []
        start_index, end_index = index_range(page, page_size)
        page_data = data[start_index:end_index]

        return page_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """using hypermedia to get next and pevious pages"""
        data = self.dataset()
        total_pages = math.ceil(len(data) / page_size)
        start_index, end_index = index_range(page, page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
                "page_size": page_size,
                "page": page,
                "data": data[start_index:end_index],
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
