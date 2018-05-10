# sorting
A collection of sorting algorithms and code to measure their running time

---

This repo contains some random code that implements a few common sorting algorithms, along with generic code to test said algs and measure their running time.

## Using the code
The actual algorithms are implemented in files with the name \*sort.py. The following algorithms are currently implemented:
* Insertion sort
* Merge sort
* Quicksort
* Selection sort

To implement a new algorithm, keep in mind: it should be a single function, which receives a list (no guarantees are made about the list being empty) and _returns_ a list. Don't rely on the list being sorted in-place (but don't rely on it being unmodified, either). You may assume that the list will only contain comparable elements.

tester.py is a crude testing facility for sorting algorithms. See the end of tester.py for an example usage. Basically, import your sorting function to tester.py and call `test_algorithm(your_sorting_function)`.

main.py and main_with_plots.py call the actual functions and record their running time. The difference is that main.py prints the running time _for a single algorithm_ for different input sizes to console, while main_with_plots.py uses matplotlib to show a scatter plot of the times _for multiple algorithms_.

plotter.m contains some helper MATLAB code that can be used to generate a scatter plot, similar to that of main_with_plots. plotter.m requires that your current MATLAB workspace contains three arrays: `sizes`, `insertion` and `merge`, of the same size, which contain, respectively, the size of the inputs and the times taken by the two algorithms to compare.
