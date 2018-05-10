from mergesort import mergesort
from insertionsort import insertionsort

import time
from random import randint

import matplotlib.pyplot as plt


def create_random_array(size):
    return [randint(0, 2 * size) for _ in range(size)]


RUNS = 25
sizes = []
insertion_times = []
merge_times = []


for size in range(5, 501, 5):
    sizes.append(size)

    avg_i = 0
    current_runs_i = 0
    avg_m = 0
    current_runs_m = 0
    for _ in range(RUNS):
        a = create_random_array(size)
        b = [x for x in a]

        start_i = time.clock()
        insertionsort(a)
        time_passed_i = time.clock() - start_i

        avg_i = avg_i * current_runs_i + time_passed_i
        current_runs_i += 1
        avg_i /= current_runs_i

        start_m = time.clock()
        mergesort(b)
        time_passed_m = time.clock() - start_m

        avg_m = avg_m * current_runs_m + time_passed_m
        current_runs_m += 1
        avg_m /= current_runs_m

    insertion_times.append(time_passed_i)
    merge_times.append(time_passed_m)


fig=plt.figure()
plt.scatter(sizes,insertion_times,label='Insertion sort')
plt.scatter(sizes,merge_times,label='Merge sort')
plt.title('Insertion sort vs. Merge sort')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo [s]')
plt.legend(loc='upper right')
plt.gca().set_ylim(bottom=0)
plt.gca().set_xlim(left=0,right=500)
plt.show()
