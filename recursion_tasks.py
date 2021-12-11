import math
from typing import List


# Task1
def binary_search_iter(Array, key):
    start = 0
    end = len(Array)-1
    while start <= end:
        mid = math.floor((start+end)/2)
        if Array[mid] == key:
            return mid
        elif Array[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


test_lst = [2, 3, 4, 10, 40, 90, 100, 101]
x = 3
# Function call
result = binary_search_iter(test_lst, x)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array")


# Binary search with recursion

def binary_search_rec(lst: List[int], key: int, start: int = 0, end: int = None):
    start = start
    if end is None:
        end = len(lst) - 1
    if start <= end:
        mid = math.floor((start + end) / 2)
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            return binary_search_rec(lst, key, start=start, end=mid - 1)
        else:
            return binary_search_rec(lst, key, start=mid + 1, end=end)
    return -1


test_lst = [2, 3, 4, 10, 40, 90, 100, 101]
x = 101
# Function call
result = binary_search_rec(test_lst, x)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array")
