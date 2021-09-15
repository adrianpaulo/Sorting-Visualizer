import timeit
import random
import matplotlib.pyplot as mat_plot_library
import numpy as numPy


def countingSort(num, arr):     # need counting sort ontop to work
    n = len(arr)

    array_output = [0] * n

    array_count = [0] * 10

    for i in range(0, n):
        index = (arr[i] / num)
        array_count[int(index % 10)] += 1

    for i in range(1, 10):
        array_count[i] += array_count[i - 1]

    i = n - 1
    # making the array_output array
    while i >= 0:
        index = (arr[i] / num)
        array_output[array_count[int(index % 10)] - 1] = arr[i]
        array_count[int(index % 10)] -= 1
        i -= 1

    i = 0
    # copying array_output into arr[]
    for i in range(0, len(arr)):
        arr[i] = array_output[i]


def radixSort(arr):
    max_value = max(arr)
    # max() returns the item with the highest value/item with the highest value in an iterable

    # counting sort for each individual digit
    i = 1
    while max_value / i > 0:
        countingSort(i, arr)
        i *= 10


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
    end_time = [10, 50, 100, 500, 1000, 5000, 10000]
    elapsed_time = []

    for i in end_time:
        array_input = []
        array_input = input(start_time, i, array_input)

        start_timer = timeit.default_timer()
        radixSort(array_input)
        elapsed_time.append(timeit.default_timer() - start_timer)

    mat_plot_library.title("Radix Sort Algorithm: ")
    mat_plot_library.xlabel("Number of Inputs: ")
    mat_plot_library.ylabel("Amount of Time: ")
    mat_plot_library.plot(end_time, elapsed_time)
    mat_plot_library.show()





