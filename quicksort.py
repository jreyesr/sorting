def quicksort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    lowers = []
    highers = []
    for x in lst[1:]:
        if x < pivot:
            lowers.append(x)
        else:
            highers.append(x)
    return quicksort(lowers) + [pivot] + quicksort(highers)
