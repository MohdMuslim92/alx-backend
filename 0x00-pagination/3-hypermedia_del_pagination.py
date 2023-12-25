#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialization
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hypermedia information based on an index.

        Args:
            index: The start index of the page.
            page_size: The number of items per page (default is 10).

        Returns:
            A dictionary containing pagination metadata and data.
        """
        assert index is None or (isinstance(
            index, int) and 0 <= index < len(self.__indexed_dataset)), \
            "Index must be in a valid range"

        if index is None:
            index = 0

        next_index = index + page_size

        while index not in self.__indexed_dataset:
            index += 1
            next_index += 1
        data = [self.__indexed_dataset[i] for i in range(
            index, min(index + page_size, len(self.__indexed_dataset)))]

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index if next_index < len(
                self.__indexed_dataset) else None,
        }
