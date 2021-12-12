from heapq import heappush, heappop
from typing import List
import random
import time
import matplotlib.pyplot as plt


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


def bubble(listas):
    indexing_length = len(listas) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if listas[i] > listas[i+1]:
                sorted = False
                listas[i], listas[i+1] = listas[i+1], listas[i]
    return listas


def quick_sort(sequance):
    length = len(sequance)
    if length <= 1:
        return sequance
    else:
        pivot = sequance.pop()

        items_greater = []
        items_lower = []

        for item in sequance:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def get_random_lists(lengths_list: List[int]) -> List[List[int]]:
    return_list = []
    for length in lengths_list:
        return_list.append([random.randint(0, 99) for _ in range(length)])
    return return_list

lists_to_test = get_random_lists([103, 152,551,666, 999, 9999])


def get_times(lists, sort_function):
    runtimes = []
    for iterable in lists:
        start = time.perf_counter()
        sort_function(iterable)
        finish = time.perf_counter()
        run_time = round(finish - start, 10)
        runtimes.append(run_time)
    return runtimes


quick_sort_results = get_times(lists_to_test, quick_sort)
bubble_sort_results = get_times(lists_to_test, bubble)
heap_sort_results = get_times(lists_to_test, heapsort)

X = [103, 152,551,666, 999, 9999]
Ya = quick_sort_results
Yb = bubble_sort_results
Yc = heap_sort_results

plt.plot(X, Ya, label="Quick")
plt.plot(X, Yb, label="Bubble")
plt.plot(X, Yc, label="Heap")
plt.legend()
plt.show()



