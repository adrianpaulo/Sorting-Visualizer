import timeit
import random
import matplotlib.pyplot as mat_plot_library
import numpy as numPy


def heapify_tree(n, i, arr):
    root = i                        # initialize the largest num into root variable
    left_side = 2 * i + 1
    right_side = 2 + 2 * i

    if left_side < n and arr[root] < arr[left_side]:    # if left root exists
        root = left_side                                # if left_side is greater than

    if right_side < n and arr[root] < arr[right_side]:  # if right root exists
        root = right_side                               # if right_side is greater than

    if root != i:                                   # swap root if root != i
        arr[i], arr[root] = arr[root], arr[i]       # error checking for root

        heapify_tree(n, root, arr)


def heapSort(arr):
    n = len(arr)

    for x in range(n // 2 - 1, -1, -1):
        heapify_tree(n, x, arr)

    for x in range(n - 1, 0, -1):
        arr[x], arr[0] = arr[0], arr[x]
        heapify_tree(x, 0, arr)


def input(startNum, endNum, arr):
    for i in range(startNum, endNum):
        # maxNum = random.randint(0, 1)                             # returns an error
        # maxNum = numPy.random.normal(0,1,1)                       # returns an error
        # maxNum = random.random()                                  # returns an error
        maxNum = pow(2, 16)
        randomNum = random.randrange(startNum, maxNum)
        arr.append(randomNum)
    return arr


if __name__ == '__main__':

    start_time = 0
    end_time = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    elapsed_time = []

    for i in end_time:
        array_input = []
        array_input = input(start_time, i, array_input)

        start_timer = timeit.default_timer()
        heapSort(array_input)
        elapsed_time.append(timeit.default_timer() - start_timer)

    mat_plot_library.title("Heap Sort Algorithm: ")
    mat_plot_library.xlabel("Number of Inputs: ")
    mat_plot_library.ylabel("Amount of Time: ")
    mat_plot_library.plot(end_time, elapsed_time)
    mat_plot_library.show()





