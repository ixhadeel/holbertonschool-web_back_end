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
        """Initialize the Server with empty cached datasets.
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
        """Return a dictionary describing a page of the indexed dataset
        that remains valid even if rows were deleted between requests.
        """
        data = self.indexed_dataset()
        assert index is not None and 0 <= index <= max(data.keys())

        page_data = []
        current_index = index
        keys_checked = 0

        while keys_checked < page_size and current_index <= max(data.keys()):
            if current_index in data:
                page_data.append(data[current_index])
                keys_checked += 1
            current_index += 1

        return {
            'index': index,
            'next_index': current_index,
            'page_size': len(page_data),
            'data': page_data,
        }
