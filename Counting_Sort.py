import timeit
import random
import matplotlib.pyplot as mat_plot_library
import numpy as numPy


def countingSort(input_arr):
    length_arr = len(input_arr)     # length of given array
    num = max(input_arr) + 1

    index = [0] * num       # index

    for v in input_arr:
        index[v] += 1

    s = 0
    for i in range(0, num):
        temp = index[i]
        index[i] = s
        s += temp

    result = [None] * length_arr
    for v in input_arr:
        result[index[v]] = v
        index[v] += 1

    return result


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
        countingSort(array_input)
        elapsed_time.append(timeit.default_timer() - start_timer)

    mat_plot_library.title("Counting Sort Algorithm: ")
    mat_plot_library.xlabel("Number of Inputs: ")
    mat_plot_library.ylabel("Amount of Time: ")
    mat_plot_library.plot(end_time, elapsed_time)
    mat_plot_library.show()





