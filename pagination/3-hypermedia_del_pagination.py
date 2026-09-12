#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize datasets."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset indexed by position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """Return a deletion-resilient page."""
        indexed_data = self.indexed_dataset()
        data_length = len(indexed_data)

        assert index is not None and 0 <= index <= data_length

        data = []
        current_index = index
        count = 0

        while count < page_size and current_index < data_length:
            row = indexed_data.get(current_index)

            if row is not None:
                data.append(row)
                count += 1

            current_index += 1

        return {
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data
        }
