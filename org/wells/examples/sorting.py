import heapq


def quick_sort(ls):
    less = []
    equal = []
    greater = []

    if len(ls) > 1:
        pivot = ls[0]
        for x in ls:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return ls


def quick_sort_test():
    print(quick_sort([3, 5, 1, 1, 7, 9, 1, 5, 13, 5, -2]))


quick_sort_test()


# min-heap sort algorithm suitable

def heapq_test():
    a = []
    heapq.heappush(a, (3, 'da3'))
    heapq.heappush(a, (2, 'da2'))
    heapq.heappush(a, (5, 'da5'))
    heapq.heappush(a, (1, 'da1'))
    heapq.heappush(a, (4, 'da4'))

    print(a)

    print(heapq.heappop(a))
    print(a)

    while len(a) > 0:
        print(heapq.heappop(a))


heapq_test()


# >>> a = [(1,5), (2,3), (2,4), (3,1),(4,3)]
# >>> a.sort(key= lambda i: i[0]+i[1])
# >>> a

def swap(a, i, j):
    if i == j:
        print('same item')
    else:
        a[i], a[j] = a[j], a[i]


def sort_3way(a, lo, hi):
    if hi <= lo:
        return
    i, lt, gt = lo, lo, hi
    v = a[lo]
    while i <= gt:
        if a[i] < v:
            swap(a, lt, i)
            lt += 1
            i += 1
        elif a[i] > v:
            swap(a, i, gt)
            gt -= 1
        else:
            i += 1
    sort_3way(a, lo, lt - 1)
    sort_3way(a, gt + 1, hi)


def qsort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    sort_3way(arr, 0, size - 1)
    return arr


def qsort_test():
    print(qsort([3, 5, 5, 6, 7, 3, 3, 6, 8, 9, 2, 4, 3, 5]))


qsort_test()
