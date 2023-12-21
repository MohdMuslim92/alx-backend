#!/usr/bin/env python3
"""
Pagination Module
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page: The page number (1-indexed).
        page_size: The number of items per page.

    Returns:
        A tuple containing the start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


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
        """
        Get a page of the dataset based on pagination parameters.

        Args:
            page: The page number (default is 1).
            page_size: The number of items per page (default is 10).

        Returns:
            A list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0, \
            "Page number must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get hypermedia information related to pagination.

        Args:
            page: The page number (default is 1).
            page_size: The number of items per page (default is 10).

        Returns:
            A dictionary containing pagination metadata.
        """
        data = self.get_page(page, page_size)
        total_pages = len(self.__dataset) // page_size + (
                1 if len(self.__dataset) % page_size != 0 else 0)

        next_page = page + 1 if page * page_size < len(
                self.__dataset) else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
