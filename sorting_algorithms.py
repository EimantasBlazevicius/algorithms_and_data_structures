bubble_list = [5,3,6,9,7,5,3,1,5,2,3,98,74,2,1,2,6,5,1]


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
# print(bubble(bubble_list))
