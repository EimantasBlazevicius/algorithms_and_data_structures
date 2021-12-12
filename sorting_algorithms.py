listas_testavimui = [0,3,6,9,7,5,3,1,5,2,3,98,74,2,1,2,6,5,1]


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
# print(bubble(listas_testavimui))


def insertion(listas):
    indexing_length = range(1, len(listas))
    for i in indexing_length:
        value_to_sort = listas[i]

        while listas[i-1] > value_to_sort and i > 0:
            listas[i], listas[i-1] = listas[i-1], listas[i]
            i = i - 1
    return listas
# print(insertion(listas_testavimui))


def selection(listas):
    indexing_length = range(0, len(listas)-1)

    for i in indexing_length:
        min_value = i
        for j in range(i+1, len(listas)):
            if listas[j] < listas[min_value]:
                min_value = j

        if min_value != i:
            listas[min_value], listas[i] = listas[i], listas[min_value]

    return listas
# print(selection(listas_testavimui))


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
# print(quick_sort(listas_testavimui))


def merge(listas):
    if len(listas) > 1:
        mid = len(listas) // 2
        left = listas[:mid]
        right = listas[mid:]

        # Recursive call on each half
        merge(left)
        merge(right)

        # two iterators to traverse two halves
        i = 0
        j = 0
        # iterator for main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # the value from the left has been used
                listas[k] = left[i]
                # move the iterator forward
                i += 1
            else:
                listas[k] = right[j]
                j += 1
            #move to the next slot
            k += 1

        # For remaining values
        while i < len(left):
            listas[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            listas[k] = right[j]
            j += 1
            k += 1

    return listas
print(merge(listas_testavimui))
