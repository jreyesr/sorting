def test_algorithm(alg):
    points = [[], [0, 1], [1, 0], [0], [0, 0], [0, 0, 0],
              [0, 1], [1, 0], [0, 1, 2], [0, 2, 1], [1, 0, 2],
              [1, 2, 0], [2, 1, 0], [2, 0, 1], [0, 0, 1],
              [0, 1, 0], [1, 0, 0], [3, 1, 2],
              [x for x in range(10)],
              [x for x in range(10)][::-1],
              [42, 9, 17, 54, 602, -3, 54, 999, -11],
              [-11, -3, 9, 17, 42, 54, 54, 602, 999]]
    oks = [[], [0, 1], [0, 1], [0], [0, 0], [0, 0, 0],
           [0, 1], [0, 1], [0, 1, 2], [0, 1, 2], [0, 1, 2],
           [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 0, 1],
           [0, 0, 1], [0, 0, 1], [1, 2, 3],
           [x for x in range(10)],
           [x for x in range(10)],
           [-11, -3, 9, 17, 42, 54, 54, 602, 999],
           [-11, -3, 9, 17, 42, 54, 54, 602, 999]]

    ok = True

    for a, b in zip(points, oks):
        new = [x for x in a]
        if(alg(new) != b):
            print(
                f"ERROR <{alg.__name__}>: {a} sorted into {new}, should be {b}")
            ok = False
    if ok:
        print(f"<{alg.__name__}> OK")


from insertionsort import insertionsort
from quicksort import quicksort
from mergesort import mergesort
from selectionsort import selectionsort

test_algorithm(quicksort)
test_algorithm(mergesort)
test_algorithm(insertionsort)
test_algorithm(selectionsort)
