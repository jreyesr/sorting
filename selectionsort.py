def selectionsort(lst):
    sorted = []
    unsorted = [x for x in lst]

    while len(sorted) < len(lst):
        i = min_elem(unsorted)
        sorted.append(unsorted[i])
        clear_elem(unsorted, i)

    lst = [x for x in sorted]
    return sorted


def min_elem(lst):
    return lst.index(min(lst))


def clear_elem(lst, i):
    del lst[i]
