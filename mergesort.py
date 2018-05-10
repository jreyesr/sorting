def mergesort(lst):
    if len(lst) <= 1:
        return lst

    left = []
    right = []
    for i, x in enumerate(lst):
        if i < len(lst) / 2:
            left.append(x)
        else:
            right.append(x)

    left = mergesort(left)
    right = mergesort(right)

    lst = [x for x in merge(left, right)]
    return lst


def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]

    return result
