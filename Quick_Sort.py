import timeit
import random
import matplotlib.pyplot as mat_plot_library
import numpy as numPy


def quickSort(arr):
    length = len(arr)

    if length < 1:          # if length of array was less than 1, return
        return arr
    else:                   # if length of array was greater than 1, set pivot point for the algorithm
        pivot = arr.pop()

    arr_of_greaterItems = []
    arr_of_lesserItems = []

    for item in arr:
        if item > pivot:
            arr_of_greaterItems.append(item)
        elif item < pivot:
            arr_of_lesserItems.append(item)

    return_var = quickSort(arr_of_lesserItems)
    return_var += [pivot]
    return_var += quickSort(arr_of_greaterItems)
    return return_var


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
        quickSort(array_input)
        elapsed_time.append(timeit.default_timer() - start_timer)

    mat_plot_library.title("Quick Sort Algorithm: ")
    mat_plot_library.xlabel("Number of Inputs: ")
    mat_plot_library.ylabel("Amount of Time: ")
    mat_plot_library.plot(end_time, elapsed_time)
    mat_plot_library.show()





