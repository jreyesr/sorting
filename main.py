from mergesort import mergesort
from insertionsort import insertionsort

import time
from random import randint


def create_random_array(size):
    return [randint(0, 2 * size) for _ in range(size)]


RUNS = 25

for size in range(5, 501, 5):
    avg = 0
    current_runs = 0
    for _ in range(RUNS):
        a = create_random_array(size)

        start = time.clock()
        insertionsort(a)
        time_passed = time.clock() - start

        avg = avg * current_runs + time_passed
        current_runs += 1
        avg /= current_runs

    print(size, avg)
