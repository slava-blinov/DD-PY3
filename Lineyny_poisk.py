"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # TODO реализовать итеративный линейный поиск
    if not arr:
        raise ValueError("Пустая последовательность")

    min_ = 0
    for index, value in enumerate(arr):
        if value < arr[min_]:
            min_ = index

    return min_
