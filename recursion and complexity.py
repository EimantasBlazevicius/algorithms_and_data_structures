import sys

sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())


def factorial(n):
    """Calculates factorial.

    Args:
        n: the natural number that is the input for the algorithm.
    Returns:
        factorial of number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n-1)


# example of input n
stringas = "laaaaaaaaaaaabbbbbbbbadsfgffdgjdejhpmhpoikm\ipbkrmnbbbbfbbbbbbcccccccccccccccz"

# O(1)
print(stringas[0])

#O(n)
for i in stringas:
    continue


#O(n * log n)
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
# print(quick_sort([4,3,7,8,2,1,6,5,9,5,4,7,8,6,3,2,1,5,6,9,8,7,54,5,6,1,855,1,2,1,4,85,5,1,51,5,4]))

#O(nc)
def loop():
    stringas = ["laaaaaa","aaaaaabbbbbbbba","dsfgffdgjdejhpmhpoikm\i","pbkrmnbbbbfbbbbbb","ccc","ccc","cccccccccz"]
    for item in stringas:
        for item2 in stringas:
            if item == item2:
                print(item2)


#O(cn)
def fibonacci_rec(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)


def fibonacci_iter(n):
    a = range(n)
    b = []

    for i in a:
        if i == a[0]:
            b.append(0)
        elif i == a[1]:
            b.append(1)
        else:
            b.append(b[i-1] + b[i-2])
    return b[-1]


for n in range(1, 99):
    print(n, ": ", fibonacci_iter(n))
